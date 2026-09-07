"""
TDD-Template für String Calculator Kata
=======================================

TODO: Team B - Entwickelt String Calculator mit TDD!

String Calculator-Regeln:
- Leerer String → 0
- Ein String mit einer Zahl → diese Zahl
- Zwei Zahlen mit Komma getrennt → Summe
- Beliebig viele Zahlen → Summe aller
- Neue Zeilen als Trenner erlaubt: "1\n2,3" → 6
- Optional: Custom Delimiter: "//;\n1;2" → 3

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
        TDD-Zyklus 1: RED von WMME
        TDD-Zyklus 1: GREEN von WMME
        TDD-Zyklus 1: REFACTOR von WMME
        TDD-Zyklus 2: RED von WMME
        TDD-Zyklus 2: GREEN von WMME
        TDD-Zyklus 2: REFACTOR von WMME
        TDD-Zyklus 3: RED von WMME
        TDD-Zyklus 3: GREEN von WMME
        TDD-Zyklus 3: REFACTOR von WMME
        TDD-Zyklus 4: RED von WMME
        TDD-Zyklus 4: GREEN von WMME
        TDD-Zyklus 4: REFACTOR von WMME
        TDD-Zyklus 5: RED von WMME
        TDD-Zyklus 5: GREEN von WMME
        TDD-Zyklus 5: REFACTOR von WMME
"""


import pytest
from ..Code.string_calculator_kata import add

# TODO: Team B - Import nach erster Implementierung:
# from ..Code.string_calculator_kata import add


class TestStringCalculatorTDD:
    """
    TODO: Team B - Entwickelt String Calculator mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_placeholder_start_here(self):
        """
        TODO: Team B - Ersetzt diesen Placeholder durch euren ersten TDD-Test!

        Ideen für den ersten Test:
        - Was ist das einfachste Verhalten?
        - add("") sollte was zurückgeben?

        TDD-Autor: [Name und Zeit]
        """
        # TODO: Euer erster TDD-Test hier
        assert add("") == 0
        assert add("1") == 1
        assert add("1,2") == 3
        assert add("1\n2,3") == 6
        #assert True, "Placeholder - startet hier mit TDD!"

        # Beispiel-Idee (entfernt nach eigenem Test):
        # assert add("") == 0


class TestStringCalculatorErweitert:
    """
    TODO: Team B - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_placeholder_extended_tests(self):
        """
        TODO: Team B - Entwickelt weitere Tests für String Calculator

        Ideen:
        - Custom Delimiters testen
        - Edge Cases (negative Zahlen, große Zahlen)
        - Parametrisierte Tests (@pytest.mark.parametrize)
        - Fehlerbehandlung (ungültige Eingaben)
        """
        # TODO: Erweiterte Tests hier
        assert add("asdf") == 0
        assert add("-1,2") == 1
        assert add("999999999,999999999") == 1999999998


# TODO: Team B - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [add("") == 0] - Autor: WMME - Zeit: [01:00]
Implementation 1: [return 0] - Zeit: [00:30]

Test 2: [add("1") == 1] - Autor: WMME - Zeit: [00:30]  
Refactoring: [return numbers] - Zeit: [00:30]

Test 3: [add("1,2") == 3] - Autor: WMME - Zeit: [00:30]  
Refactoring: [Funktion zum Splitten und addieren] - Zeit: [10:00]

Test 4: [add("1\n2,3") == 6] - Autor: WMME - Zeit: [00:30]  
Refactoring: [\n wird zum Splitten durch , ersetzt] - Zeit: [02:00]

Test 5: [erweiterte Tests] - Autor: WMME - Zeit: [03:00]  
Refactoring: [if number.lstrip("-").isdigit():] - Zeit: [03:00]



Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
- Unterschiede zu FizzBuzz?
"""
