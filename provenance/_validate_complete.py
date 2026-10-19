from pathlib import Path
import json,re,html,hashlib,sys
w=Path(__file__).parent;sys.path.insert(0,'/Volumes/LaCie/open-commentary/_tools');from build_repo import load_commentary
units=[json.loads(l) for l in (w/'units.jsonl').read_text().splitlines()];meta=json.loads((w/'meta.json').read_text());repo=Path(meta['repo_dir']);raw=(w/'sources/snapshot-official.html').read_text();cov=json.loads((w/'coverage-evidence.json').read_text());com=load_commentary(w)
expected=re.findall(r'<article\b[^>]*\bid="([^"]+)"',raw)
if '<section id="disp_u1">' in raw:expected.append('disp_u1')
assert expected==cov['expected_ids']==cov['parsed_ids']==[u['id'] for u in units]
assert len(expected)==len(set(expected)) and set(com)==set(expected)
assert cov['annex_disposition'] and not re.findall(r'<(?:section|div|article)\b[^>]*id="(?:annex|annexe|anhang)',raw,re.I)
# Independent extraction of raw markup: does not invoke the production DOM parser.
failed=[]
for u in units:
 if u['id']=='disp_u1':frag=re.search(r'<section id="disp_u1">(.*?)</section>',raw,re.S)[1]
 else:frag=re.search(r'<article id="'+re.escape(u['id'])+r'">(.*?)</article>',raw,re.S)[1]
 frag=re.sub(r'<h[1-6]\b.*?</h[1-6]>','',frag,flags=re.S)
 frag=re.sub(r'<div class="footnotes[^\"]*">.*?</div>','',frag,flags=re.S)
 frag=re.sub(r'<a\b[^>]*id="fnbck-[^\"]*"[^>]*>.*?</a>','',frag,flags=re.S)
 text=html.unescape(re.sub(r'<[^>]+>','',frag));norm=lambda x:re.sub(r'\s+','',x)
 if norm(text)!=norm(u['text']):failed.append(u['id'])
assert not failed,failed
notes=json.loads((w/'sources/footnotes.json').read_text())
expected_note_ids=re.findall(r'<p\b[^>]*\bid="(fn-[^"]+)"',raw)
assert [x['id'] for x in notes]==expected_note_ids
assert len(notes)==60 and len(set(expected_note_ids))==60
assert cov['footnotes']['expected_ids']==cov['footnotes']['extracted_ids']==expected_note_ids
outside=[x for x in notes if not x['owner_id'].startswith('art_')]
assert len(outside)==8
for note in notes:
 if note['owner_id'].startswith('art_'):
  unit=next(u for u in units if u['id']==note['owner_id'])
  assert any(note['text'] in n for n in unit['notes']),note['id']
 else:assert note['text'] in (w/'AMTLICHE-STRUKTUR.md').read_text(),note['id']
for chapter in meta['chapters']:
 members=[u for u in units if u['chapter']==chapter['n']]
 assert '**Praxischeck zum Kapitel:**' in com[members[-1]['id']]
 assert all('**Praxischeck zum Kapitel:**' not in com[u['id']] for u in members[:-1])
assert all(len(com[u['id']])>=(120 if len(u['text'])<160 else 400) for u in units)
assert all(len(com[u['id']])>=700 for u in units if not u['repealed'] and not u.get('empty_slot'))
seen={};duplicates=[]
for uid,c in com.items():
 for p in c.split('\n\n'):
  if len(p)>180:
   if p in seen:duplicates.append([seen[p],uid])
   seen[p]=uid
assert not duplicates,duplicates
chapters={c['n']:c for c in meta['chapters']};bad=[]
for u in units:
 c=chapters[u['chapter']];fp=repo/f"{c['n']:02d}-{c['slug']}.md"
 if fp.exists():assert com[u['id']] in fp.read_text()
for p in repo.glob('*.md'):
 for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in link and not link.startswith('#') and not (p.parent/link.split('#')[0]).exists():bad.append([p.name,link])
assert not bad,bad
assert (repo/'LICENSE').read_bytes()==Path('/Volumes/LaCie/open-commentary/_tools/LICENSE').read_bytes()
assert all(p.read_bytes()==(repo/'sources'/p.name).read_bytes() for p in (w/'sources').iterdir() if p.is_file())
report=dict(ok=True,statutory_units=len(units),expected_ids_independent=True,parsed_ids_match=True,annex_disposition=cov['annex_disposition'],raw_character_sequence_all_units=True,footnotes_complete=True,footnote_count=len(notes),non_article_footnotes_preserved=len(outside),chapter_end_checklists_correct=True,chapter_commentary_match=True,all_ordinary_comments_700_plus=True,no_repeated_long_paragraphs=True,local_links_ok=True,source_copies_exact=True,license_exact=True,commentary_chars=sum(map(len,com.values())),technical_check_not_substantive_review=True)
print(json.dumps(report,ensure_ascii=False))
