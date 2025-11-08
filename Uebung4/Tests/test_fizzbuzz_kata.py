"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest

# TODO: Team A - Import nach erster Implementierung:
# from Teil2_TDD_und_Mocking.aufgaben.fizzbuzz_kata import fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_placeholder_start_here(self):
        """
        TODO: Team A - Ersetzt diesen Placeholder durch euren ersten TDD-Test!

        Ideen für den ersten Test:
        - Was ist das einfachste Verhalten?
        - fizzbuzz(1) sollte was zurückgeben?

        TDD-Autor: [Name und Zeit]
        """
        eingabe1 = 1
        erwartetes_ergebnis1 = str("1")
        eingabe2 = 3
        erwartetes_ergebnis2 = str("Fizz")
        eingabe3 = 5
        erwartetes_ergebnis3 = str("Buzz")
        eingabe4 = 15
        erwartetes_ergebnis4 = str("FizzBuzz")

        assert fizzbuzz(eingabe1) == erwartetes_ergebnis1
        assert fizzbuzz(eingabe2) == erwartetes_ergebnis2
        assert fizzbuzz(eingabe3) == erwartetes_ergebnis3


class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    """
    @pytest.mark.parametrize("n, expected", [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (9, "Fizz"),
        (10, "Buzz"),
    ])
    
    def test_placeholder_extended_tests(n, expected):
        assert fizzbuzz(n) == expected


# TODO: Team A - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [Was getestet] - Autor: [Name] - Zeit: [Zeit]
Implementation 1: [Minimale Lösung] - Zeit: [Zeit]

Test 2: [Was getestet] - Autor: [Name] - Zeit: [Zeit]  
Refactoring: [Was geändert] - Zeit: [Zeit]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
"""
