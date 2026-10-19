# Quellenkarte — SR 221.213.2

## Amtlicher Normtext und aktuelle Version

- [Fedlex HTML](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1986/926_926_926/20140101/de/html/fedlex-data-admin-ch-eli-cc-1986-926_926_926-20140101-de-html-14.html), [PDF](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1986/926_926_926/20140101/de/pdf-a/fedlex-data-admin-ch-eli-cc-1986-926_926_926-20140101-de-pdf-a.pdf).
- HTML-Abruf: 2026-10-19T12:43:13.475428+00:00, HTTP 200, SHA-256 `97ef3602b5e93c54edeee3b03d6e8dee812074566a36c7c90a8c9797ce835339`.
- PDF-Abruf: 2026-10-19T12:45:57.125360+00:00, HTTP 200, SHA-256 `a6837d657d9eb52b46dfb47f423077e5a29b019c061bde75829ef0021bb4d132`.
- Aktuellste effektive Konsolidierung: 2014-01-01; geprüft durch Mitgliederinventar und `dateApplicability`, nicht nur anhand des Abrufdatums.
- [Verifikationsmanifest](sources/verification.json), [Versionsinventar](sources/versions-query-confirmation.json), [Metadaten der Fassung](sources/version-details.json).
- [Original-HTML](sources/snapshot-official.html), [Original-PDF](sources/official.pdf), [PDF-Lesefassung](sources/official-pdf.txt), [kanonische Parserableitung](sources/canonical.md).

## Snapshotvergleich und Textbesonderheiten

Die unveränderte Intake-Kopie ist in [intake-original.md](sources/intake-original.md) mit SHA-256 `4d39abaae99efd4cd04c8edb818e2a6d31b0d6f1ef5d7298e1a0c07768a79e9d` erhalten. [Änderungskarte](sources/change-map.json): keine inhaltliche Gesetzesänderung; lediglich Layout- und Fussnotenmarker werden normalisiert. Die eigene kanonische Quelle ersetzt keine Originalverkündung. Keine Änderung am globalen Intake.

Die materiellen Texte werden aus dem aktuellen amtlichen Abruf extrahiert. Absätze mit Auslassungszeichen bleiben erhalten. Gruppierte Aufhebungen werden wie amtlich in einer Einheit dargestellt; sie verschwinden weder aus dem Inventar noch werden sie als neue Einzeltexte rekonstruiert. [Deckungsnachweis](coverage-evidence.json).

## Nachprüfbarkeit und Grenzen

Parser und Einheiten sind unter `provenance/` beigefügt. Für Reproduktion den Parser mit `assignment.json` und `sources/` in ein separates Arbeitsverzeichnis kopieren; Ausgabeziele vorher anpassen, damit kein fertiger Stand überschrieben wird. Die amtliche Fussnoten- und Absatzstruktur bleibt im Rohtext überprüfbar. [Prüfergebnis](completeness.json). Ein Hash belegt Dateiintegrität, keine materielle Richtigkeit.

[Rechtsprechungskarten](RECHTSPRECHUNG.md) beschreiben tatsächlich ausgewertete amtliche publizierte Auszüge; direkte Bot-Schutzantworten wurden verworfen. Nicht jedes Ausführungsrecht und nicht jede historische Änderung ist vollständig untersucht. Alle Quellenartefakte sind im lokalen Hashmanifest erfasst.

## Zweitprüfung am 19. Oktober 2026

Fedlex-HTML, Versionsinventar und Anwendbarkeitsmetadaten wurden erneut mit HTTP 200 abgerufen; die Körper stimmen bytegenau mit der Erstprüfung überein. [Neue Abrufbelege](sources/review-retrieval.json). Die jüngste ausgewiesene Konsolidierung bleibt der 1. Januar 2014. [Ingress und Gliederungsanmerkungen](AMTLICHE-STRUKTUR.md) ergänzen die artikelbezogenen Fussnoten; [Gesamtinventar aller 60 Fussnoten](sources/footnotes.json). Die erneut über Firecrawl bezogenen amtlichen BGE-Auszüge stammen laut Metadaten aus dem Cache desselben Prüftags; dies ist kein behaupteter neuer Direktabruf am Gerichtsserver. [Sachliche Zweitprüfung](REVIEW.md).
