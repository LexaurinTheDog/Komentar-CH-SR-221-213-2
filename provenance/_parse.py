from html.parser import HTMLParser
from pathlib import Path
import re,json,hashlib
class Node:
 def __init__(self,t,a):self.tag=t;self.attrs=dict(a);self.items=[]
 def all(self):
  yield self
  for c in self.items:
   if isinstance(c,Node):yield from c.all()
 def text(self,notes=False):
  if not notes and ('footnotes' in self.attrs.get('class','') or self.attrs.get('id','').startswith('fnbck-')):return ''
  out=''
  for c in self.items:
   if isinstance(c,str):out+=c
   elif c.tag=='br':out+='\n'
   else:
    t=c.text(notes)
    if c.tag in ['p','dl','dt','dd','li']:out+='\n\n'+t+'\n\n'
    else:out+=t
  return out
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.root=Node('root',[]);self.stack=[self.root]
 def handle_starttag(self,t,a):
  n=Node(t,a);self.stack[-1].items.append(n)
  if t not in ['meta','link','br','img','hr','input']:self.stack.append(n)
 def handle_endtag(self,t):
  for i in range(len(self.stack)-1,0,-1):
   if self.stack[i].tag==t:self.stack=self.stack[:i];break
 def handle_data(self,s):self.stack[-1].items.append(s)
def clean(s):return '\n\n'.join(re.sub(r'\s+',' ',p).strip() for p in re.split(r'\n\s*\n',s) if p.strip())
def parse(path):
 p=Parser();p.feed(path.read_text());return p.root

def main():
 w=Path(__file__).parent;j=json.loads((w/'assignment.json').read_text());raw=w/'sources/snapshot-official.html';root=parse(raw);units=[];chapters=[]
 def walk(n,structure=[],chapter=0):
  if n.tag=='section' and not n.attrs.get('id','').startswith('disp'):
   h=next((c for c in n.items if isinstance(c,Node) and c.tag.startswith('h')),None)
   if h:
    title=clean(h.text());structure=structure+[title]
    if '/' not in n.attrs.get('id',''):
     chapter=len(chapters)+1;chapters.append(dict(n=chapter,slug='kapitel-'+str(chapter),title=title))
  uid=n.attrs.get('id','')
  if n.tag=='article' or uid=='disp_u1':
   h=next((c for c in n.items if isinstance(c,Node) and c.tag.startswith('h')),None);heading=clean(h.text())
   body=next((c for c in n.items if isinstance(c,Node) and c.tag=='div' and 'collapseable' in c.attrs.get('class','')),None)
   text=clean(body.text()) if body else ''
   label=re.match(r'Art\.\s*\d+[a-z]*(?:[−–-]\d+| und \d+)?',heading).group() if heading.startswith('Art.') else heading
   title=heading[len(label):].strip();notes=[clean(x.text(True)) for x in n.all() if 'footnotes' in x.attrs.get('class','')]
   if uid=='disp_u1':
    chapter=len(chapters)+1;chapters.append(dict(n=chapter,slug='schlussbestimmungen-1998',title=heading));structure=[heading]
   units.append(dict(id=uid,label=label,title=title,text=text,notes=notes,chapter=chapter,structure=structure,repealed=(not text and any('Aufgehoben' in x for x in notes)) or text in ['…','...'] or bool(re.search('Aufgehoben',text))))
   return
  for c in n.items:
   if isinstance(c,Node):walk(c,structure,chapter)
 walk(root)
 assert all(u['chapter'] for u in units)
 for u in units:u['empty_slot']=not bool(u['text'])
 (w/'units.jsonl').write_text(''.join(json.dumps(u,ensure_ascii=False)+'\n' for u in units))
 canon='\n\n'.join(u['label']+' '+u['title']+'\n\n'+u['text'] for u in units)
 (w/'sources/canonical.md').write_text(canon)
 meta=dict(cc='ch',lang='de',repo=j['repo'],repo_dir=j['output'],title='Kommentar: '+j['title'],source_path=str(w/'sources/canonical.md'),intro_file='00-einleitung.md',intro_desc='Grundlagen, Stand und Methode',labels=dict(text='Wortlaut der Vorschrift',chapter='Kommentarkapitel',notes='Amtliche Anmerkung'),chapters=chapters)
 (w/'meta.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 # Independent expected inventory from raw official markup, without parser output.
 s=raw.read_text();expected=re.findall(r'<article\b[^>]*\bid="([^"]+)"',s)
 if re.search(r'<section\b[^>]*\bid="disp_u1"',s):expected.append('disp_u1')
 parsed=[u['id'] for u in units];assert expected==parsed and len(set(parsed))==len(parsed)
 annex_ids=re.findall(r'<(?:section|div|article)\b[^>]*\bid="((?:annex|annexe|anhang)[^"]*)"',s,re.I)
 assert not annex_ids,annex_ids
 coverage=dict(official_source=dict(url=j['source_url'],local_raw_evidence_path=str(raw),sha256=hashlib.sha256(raw.read_bytes()).hexdigest()),expected_ids=expected,parsed_ids=parsed,expected_derivation='Unabhängige reguläre Inventarisierung sämtlicher article-ID-Attribute und der selbständigen Schlussbestimmung disp_u1 im amtlichen Roh-HTML; nicht aus units.jsonl kopiert.',annex_disposition='Im gesamten amtlichen Roh-HTML keine eigenständige Anlage/kein Anhang vorhanden; Schlussbestimmungen und aufgehobene Sammelstellen sind ausdrücklich einbezogen.',repealed_slots=[dict(id=u['id'],label=u['label']) for u in units if u['repealed']],empty_slots=[dict(id=u['id'],label=u['label'],repealed=u['repealed']) for u in units if u['empty_slot']],missing_ids=[],duplicate_ids=[],ok=True)
 (w/'coverage-evidence.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
 # Preserve notes belonging to the preamble/structural headings, separately
 # from article notes; do not attach them to an unrelated numbered provision.
 footnotes=[]
 def collect(n,ancestors):
  if n.tag=='p' and n.attrs.get('id','').startswith('fn-'):
   owner=next((a for a in reversed(ancestors) if a.tag=='article' or a.attrs.get('id')=='preamble' or a.tag=='section'),None)
   footnotes.append(dict(id=n.attrs['id'],number=int(clean(n.text(True)).split()[0]),owner_id=owner.attrs.get('id') if owner else None,text=clean(n.text(True))))
  for c in n.items:
   if isinstance(c,Node):collect(c,ancestors+[n])
 collect(root,[])
 expected_notes=re.findall(r'<p\b[^>]*\bid="(fn-[^"]+)"',s)
 assert expected_notes==[f['id'] for f in footnotes]
 assert len(expected_notes)==len(set(expected_notes))
 (w/'sources/footnotes.json').write_text(json.dumps(footnotes,ensure_ascii=False,indent=2))
 preamble=next(n for n in root.all() if n.attrs.get('id')=='preamble')
 extra=[f for f in footnotes if not f['owner_id'].startswith('art_')]
 md='# Amtlicher Ingress und Anmerkungen zur Gliederung\n\nMechanische Ergänzung aus dem gesicherten [Fedlex-HTML](sources/snapshot-official.html), Stand 1. Januar 2014, geprüft am 19. Oktober 2026. Diese amtlichen Anmerkungen sind vom eigenen Kommentar getrennt. Artikelbezogene Anmerkungen stehen bei den Artikeln; das [Gesamtinventar](sources/footnotes.json) erfasst alle 60 Fussnoten.\n\n## Ingress\n\n'
 md+='\n>\n'.join('> '+p for p in clean(preamble.text()).split('\n\n'))+'\n\n## Anmerkungen ausserhalb der Artikel\n\n'
 for f in extra:
  md+=f"### Fussnote {f['number']} — `{f['owner_id']}`\n\n> {f['text']}\n\n"
 (w/'AMTLICHE-STRUKTUR.md').write_text(md)
 coverage['footnotes']={'expected_ids':expected_notes,'extracted_ids':[f['id'] for f in footnotes],'total':len(footnotes),'outside_articles':len(extra),'disposition':'Artikelanmerkungen in units.jsonl; Ingress und acht strukturelle Anmerkungen in AMTLICHE-STRUKTUR.md; alle Anmerkungen mit amtlicher ID in sources/footnotes.json.'}
 (w/'coverage-evidence.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
 print(j['repo'],len(units),'units',len(chapters),'chapters')
if __name__=='__main__':main()
