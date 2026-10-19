# Einleitung — LPG

## Gegenstand und überprüfter Stand

Bundesgesetz vom 4. Oktober 1985 über die landwirtschaftliche Pacht (LPG), SR 221.213.2. Verwendete deutsche Fedlex-Fassung mit Anwendbarkeitsdatum **2014-01-01**. Quellenprüfung am 19.10.2026. Über die amtliche SPARQL-Struktur wurden sämtliche als `isMemberOf` ausgewiesenen Konsolidierungen abgefragt; die jüngste bis zum Bearbeitungsstichtag ist die verwendete Fassung. Das `dateApplicability`-Metadatum bestätigt den Geltungsbeginn. Eine bloss neu abgerufene alte URL oder technische Änderungszeit wäre dafür kein ausreichender Nachweis. Die ebenfalls registrierten Projekte sind nicht als bereits geltende Änderungen behandelt.

## Umfang und Extraktion

Vollständige Kommentierung von 64 amtlichen Einheiten in 7 Kapiteln. Nummerierte Artikel, amtlich gruppierte Aufhebungen und selbständige Schlussbestimmungen werden erhalten. Keine rechtlich operative Anlage im amtlichen HTML oder PDF vorhanden. Der Parser übernimmt den Norminhalt mechanisch; Absatznummern und Listen bleiben in der Hierarchie lesbar, blosse Fussnotenmarker werden vom Normtext getrennt. Artikelbezogene amtliche Anmerkungen bleiben bei den Einheiten; der [Ingress und die Anmerkungen zur Gliederung](AMTLICHE-STRUKTUR.md) werden gesondert wiedergegeben. Das [Fussnoteninventar](sources/footnotes.json) erfasst alle 60 Anmerkungen mit ihren amtlichen IDs und ihrer Zuordnung. Leere aufgehobene Stellen werden nicht mit erfundenem Gesetzestext gefüllt.

Die `expected_ids` in [coverage-evidence.json](coverage-evidence.json) werden unabhängig durch Inventarisierung der IDs im Roh-HTML ermittelt und mit den Parser-IDs abgeglichen. Das amtliche PDF ist als zweites Format gesichert; die kritischen Leer- und Sammelstellen wurden darin geprüft. Eine Längenprüfung allein beweist weder Vollständigkeit noch juristische Qualität. Der globale Intake wird nicht verändert; seine unveränderte Kopie und der [Änderungsabgleich](sources/change-map.json) bleiben erhalten. Der aktuelle Abruf zeigt keinen inhaltlichen Versionswechsel gegenüber diesem Snapshot.

## Methode der Erläuterung

Jede Einheit erhält einen eigenen Auslegungstext zu Funktion, tatsächlichen Merkmalen, Folgen und Zusammenhang. Beispiele sind erfundene Anwendungsfälle, keine behaupteten Gerichtsentscheidungen. Am Ende jedes Kapitels stehen konkrete Praxisprüfungen. [Fallbeispiele](FALLBEISPIELE.md) verbinden mehrere Normen. Externe Gesetze, Verordnungen, kantonale Regeln und Gesamtarbeitsverträge werden nur im ausgewiesenen Umfang erläutert; konkrete aktuelle Berechnungswerte werden nicht ohne Quelle ergänzt.

## Rechtsprechung und Status

[RECHTSPRECHUNG.md](RECHTSPRECHUNG.md) trennt ausgewertete amtliche Entscheidungen, deren zeitliche Grenzen und nicht vollständig recherchierte Fragen. Keine Aussage, alle einschlägigen Entscheidungen seien gefunden oder es gebe zu anderen Artikeln keine Rechtsprechung. Historische Zwischenfassungen und sämtliche Ausführungsverordnungen sind nicht vollständig kommentiert.

Status: vollständig ausgearbeiteter Entwurf nach einer unabhängigen zweiten Durchsicht aller 64 Einheiten, siehe [Prüfbericht](REVIEW.md). Keine externe fachanwaltliche oder wissenschaftliche Freigabe. Vor Mandatsverwendung sind konkreter Sachverhalt, Zeitfassung, Ausführungsrecht und Verfahrensfristen erneut zu prüfen. Kommentartext © 2026 Vojtěch Říha, Apache-2.0. Die Lizenz betrifft eigene Beiträge; amtliche Quellen und deren Herkunft sind getrennt ausgewiesen. Bereitstellung wie vorhanden, keine individuelle Rechtsberatung.
