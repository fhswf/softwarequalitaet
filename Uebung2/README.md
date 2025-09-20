# Übungsblatt 2: Konstruktive Softwarequalität mit GitHub Codespaces

In dieser Übung analysieren Sie bestehenden Python-Code im Hinblick auf die Prinzipien konstruktiver Softwarequalität. Idealerweise nutzen Sie GitHub Codespaces als cloudbasierte Entwicklungsumgebung.

## Konstruktive Softwarequalität

Konstruktive Qualitätssicherung zielt darauf ab, Fehler frühzeitig zu vermeiden, statt sie erst im Nachhinein zu finden. Typische Maßnahmen sind:

- saubere Code-Struktur und gute Lesbarkeit,
- Einhaltung von Coding-Konventionen,
- Durchführung von Code-Reviews,
- Modularisierung und klare Verantwortlichkeiten.

Diese Prinzipien helfen, Software testbar, wartbar und robust zu gestalten. In dieser Übung sehen Sie Sich bestehenden Code an und verbessern ihn unter konstruktiven Gesichtspunkten.

# Aufgaben zur Datei Uebung2.py

## Allgemeine Hinweise

- Die Datei [`Uebung2.py`](./Uebung2.py) befindet sich im selben Ordner wie diese `README.md`.
- Arbeiten Sie in Ihrer Kleingruppe an den Aufgaben.
- Verwenden Sie Pair-Programming (ideal: 2 Personen; Gruppen bis zu 3 Personen sind möglich). Teilen Sie sich gegebenenfalls in kleinere Teams innerhalb Ihrere Gruppe auf.
- Falls mehrere Teams innerhalb einer Gruppe parallel arbeiten, kopieren Sie die Code-Datei und benennen Sie diese um, z. B. in `Uebung2-TeamA.py` und `Uebung2-TeamB.py`.
- Die Dateien sollen später von einer anderen Gruppe gereviewed werden. Falls Sie keine Repository innerhalb der FH-SWF-Organisation verwenden, müssen Sie entweder Ihre Lösungsdateien oder den Link zum öffentlichen Repository unter Angabe Ihrer Gruppennummer **bis zum nachfolgenden Montag** per Mail an den Modulverantwortlichen senden.

## Aufgabenstellung

Bearbeiten Sie die folgenden Punkte in Ihrer Kleingruppe. Schreiben Sie zu Beginn die Kürzel aller Teilnehmer (erster und letzter Buchstabe des Vornamens + erster und letzter Buchstabe des Nachnamens; Beispiel für "Hans Wurst": "HSWT") als Kommentar oben in die Datei. Erstellen Sie nach jeder Aufgabe einen Commit und pushen Sie diesen in Ihr Gruppenrepository. Die Commit-Nachricht sollte die durchgeführte Aufgabe beschreiben (z. B. `Ü2-A1 Funktionen des Codes`).

### Aufgabe 1

Welche Funktionen erfüllt der vorliegende Code?
Verschaffen Sie Sich zunächst einen Überblick über die Funktionalität, z. B. indem Sie den Code ausführen und die Aufrufe am Ende der Datei verändern. Ändern Sie in diesem Schritt die Zeilen oberhalb von Zeile 82 noch nicht. Notieren Sie stichpunktartig als Blockkommentar ganz oben in der Datei, welche Stellen das Verständnis des Codes erschweren.

(Zeit: ca. 10 min)

### Aufgabe 2

Welche Aspekte des Codes sind aus Sicht der Softwarequalität positiv bzw. negativ zu bewerten?
Beachten Sie dabei z. B. Struktur, Lesbarkeit, Verständlichkeit, Dokumentation, Robustheit, Fehlervermeidung und Wartbarkeit. Fügen Sie einen weiteren Blockkommentar oben in der Datei hinzu mit einer Liste möglicher Verbesserungen.

(Zeit: ca. 10 min)

### Aufgabe 3

Verbessern Sie den Code gezielt. Kommentieren Sie Ihre Änderungen im Code und erstellen Sie Zwischencommits mit aussagekräftigen Commit-Nachrichten, z. B.:

- `Kommentare hinzugefügt`
- `Methodennamen verbessert`
- `Fehlende Rückgabewerte ergänzt`

(Zeit: ca. 30 min)

### Aufgabe 4 _(optional)_

Führen Sie optional eine automatisierte Code-Qualitätsanalyse mit _Pylint_ durch und dokumentieren Sie die wichtigsten Ergebnisse.

#### Was ist _Pylint_?

Pylint ist ein Analysewerkzeug für Python-Code, das automatisch auf Programmierfehler, Stilabweichungen und potenziell problematische Konstrukte hinweist. Es hilft dabei, die Codequalität zu verbessern, indem es Hinweise zu Lesbarkeit, Namenskonventionen und möglichen Bugs liefert. Besonders nützlich ist Pylint in der frühen Entwicklungsphase, um typische Fehler zu vermeiden und konsistenten, wartbaren Code zu schreiben.

#### Vorgehen

Falls Sie keinen DevContainer oder Codespace verwenden:
Öffnen Sie ein Terminal und installieren Sie bei Bedarf Pylint:

`pip install pylint`

Führen Sie dann auf Ihrer bereits veränderten Datei folgende Schritte aus:

1. Navigieren Sie zum Ordner mit der Python-Datei:

   `cd "Uebungen/Uebungsblatt2"`

2. Führen Sie Pylint aus:

   `python -m pylint Uebung2-TeamA.py`

Schauen Sie Sich die Ergebnisse der Analyse an. Pylint zeigt unter anderem:

- **Score**: Bewertung von 0–10 (10 = perfekt)
- **Kategorien**:
  - C = Convention
  - R = Refactor
  - W = Warning
  - E = Error
  - F = Fatal
- **Zeilennummern** der betroffenen Stellen

Eine Liste der Pylint-Codes zur Interpretation der Ergebnisse finden Sie in der offiziellen Doku: https://pylint.readthedocs.io/en/stable/user_guide/messages/.

Erstellen Sie einen Blockkommentar ganz unten in der Datei und fügen Sie dort den Pylint-Output ein. Kommentieren Sie jede relevante Zeile kurz, ob Sie der Anmerkung zustimmen oder nicht (inkl. kurzer Begründung). Ändern Sie anschließend den Code, um einige der gefundenen Punkte zu beheben. Versuchen Sie, die Punktzahl zu verbessern.
