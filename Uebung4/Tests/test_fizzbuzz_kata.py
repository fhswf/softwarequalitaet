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
from Uebung4.Code.fizzbuzz_kata import fizzbuzz

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
    
    def test_placeholder_extended_tests(self, n, expected):
        assert fizzbuzz(n) == expected


class TestFizzBuzzErweitert_2:
    def test_erweitert_2(self):
        eingabe1 = 0
        erwartetes_ergebnis1 = str("FizzBuzz")
        
        assert fizzbuzz(eingabe1) == erwartetes_ergebnis1

class TestFizzBuzzErweitert_3:
    def test_erweitert_2(self):
        eingabe1 = -3
        erwartetes_ergebnis1 = str("Fizz")
        
        assert fizzbuzz(eingabe1) == erwartetes_ergebnis1

class TestFizzBuzzErweitert_4:
    def test_erweitert_2(self):
        eingabe1 = -30
        erwartetes_ergebnis1 = str("FizzBuzz")
        
        assert fizzbuzz(eingabe1) == erwartetes_ergebnis1


# Team A - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Test 1: [test_placeholder_start_here - einfache Implementierung von ein paar Fällen] - Autor: [CRVA] - Zeit: [10:45]
Implementation 1: [return str("FizzBuzz")]] - Zeit: [10:50]

Test 2: [test_placeholder_extended_tests - verschiedene Fälle] - Autor: [CRVA] - Zeit: [11:30]  
Refactoring: [nicht wirklich was] - Zeit: [11:40]

[Weiter dokumentieren...]

Erkenntnisse:
- Was war überraschend?: Negative Zahlen werden richtig behandelt
- Wo musstet ihr refaktorieren?: Unsicher: Ist soll die 0 nun FizzBuzz zurückgeben oder einen anderen Wert???
- Welche Tests brachten neue Herausforderungen?
"""
