"""
Test-Template für die Konto-Klasse (Test-After Approach)
========================================================

TODO: Team A - Implementieren Sie hier Ihre Tests NACH der Konto-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die Konto-Klasse in Code/konto.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Code
3. Testen Sie normale Fälle UND Grenzfälle
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für gute Tests:
- Verwenden Sie aussagekräftige Test-Namen
- Testen Sie eine Sache pro Test
- Nutzen Sie pytest.raises() für Exception-Tests
- Denken Sie an Grenzwerte (0, negative Zahlen)
"""

import pytest
from decimal import Decimal
from Uebung3.Code.konto import *


class TestKontoErstellung:
    """
    Tests für die Konto-Erstellung
    TODO: Team A - Implementieren Sie Tests für den Konstruktor
    """

    def test_placeholder_konto_erstellung(self):
        # Konto mit gültiger ID und positivem Saldo erstellen
        konto = Konto(1, Decimal("100.00"))
        assert konto # konto ist nicht 'Null' / None
        assert konto.konto_id == 1
        assert konto.saldo == Decimal("100.00")

        # Konto mit gültiger ID und Saldo 0 erstellen
        konto = Konto(2, Decimal("0.00"))
        assert konto.konto_id == 2
        assert konto.saldo == Decimal("0.00")

        # Konto mit ungültiger ID (negativ, 0, String) → Exception?
        with pytest.raises(TypeError) as exception_info:
            konto = Konto(0, Decimal("0.00"))
        assert "Konto-ID muss eine ganze Zahl > 0 sein." in exception_info.value

        with pytest.raises(TypeError) as exception_info:
            konto = Konto("Hello", Decimal("0.00"))
        assert "Konto-ID muss eine ganze Zahl > 0 sein." in exception_info.value

        with pytest.raises(TypeError) as exception_info:
            konto = Konto(-123, Decimal("0.00"))
        assert "Konto-ID muss eine ganze Zahl > 0 sein." in exception_info.value

        # Konto mit ungültigem Saldo (negativ, String) → Exception?
        with pytest.raises(ValueError) as exception_info:
            konto = Konto(3, Decimal("-50.45"))
        assert konto.konto_id == 3
        assert "Startsaldo darf nicht negativ sein." in exception_info.value

        with pytest.raises(TypeError) as exception_info:
            konto = Konto(4, "Hello!")
        assert konto.konto_id == 4
        assert "Saldo muss Typ Decimal sein." in exception_info.value




class TestKontoEigenschaften:

    def test_placeholder_eigenschaften(self):
        test_id = 1
        startsaldo = Decimal("100.00")
        konto = Konto(test_id, startsaldo)
        
        # - konto.konto_id gibt korrekte ID zurück
        assert konto.konto_id == test_id

        # - konto.saldo gibt korrekten Saldo zurück
        assert konto.saldo == startsaldo
        
        # - Properties sind read-only (falls gewünscht)
        with pytest.raises(AttributeError) as exception_info: 
            konto.konto_id = 10
        assert "AttributeError" in exception_info.typename

        with pytest.raises(AttributeError) as exception_info: 
            konto.saldo = Decimal("12.13")
        assert "AttributeError" in exception_info.typename
        



class TestEinzahlung:
    """
    Tests für die Einzahlungs-Funktionalität
    TODO: Team A - Testet alle Einzahlungs-Szenarien
    """

    def test_placeholder_einzahlung(self):
        startbetrag = Decimal("100.00")
        einzahlungsbetrag = Decimal("10.00")
        konto = Konto(1, startbetrag)
        
        # - Einzahlung von positivem Betrag
        # - Saldo wird korrekt erhöht
        konto.einzahlen(einzahlungsbetrag)
        assert konto.saldo == startbetrag + einzahlungsbetrag
        
        # - Einzahlung von 0 → Exception?
        with pytest.raises(Einzahlungsfehler): 
            konto.einzahlen(Decimal("0.00"))

        # - Einzahlung von negativem Betrag → Exception?
        with pytest.raises(Einzahlungsfehler): 
            konto.einzahlen(Decimal("-123.00"))

        # - Einzahlung von ungültigem Typ → Exception?
        with pytest.raises(Einzahlungsfehler): 
            konto.einzahlen("Hello!")


class TestAuszahlung:

    def test_placeholder_auszahlung(self):
        startbetrag = Decimal("100.00")
        auszahlungsbetrag = Decimal("10.00")
        auszuahlungsbetrag_zu_hoch = Decimal("500.00")
        konto = Konto(1, startbetrag)
        
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        konto.auszahlen(auszahlungsbetrag)
        assert konto.saldo == startbetrag - auszahlungsbetrag

        # - Auszahlung bei unzureichendem Saldo → Exception?
        with pytest.raises(Auszahlungsfehler):
            konto.auszahlen(auszuahlungsbetrag_zu_hoch)

        # - Auszahlung von 0 → Exception?
        with pytest.raises(Auszahlungsfehler):
            konto.auszahlen(Decimal("0.00"))

        # - Auszahlung von negativem Betrag → Exception?
        with pytest.raises(Auszahlungsfehler):
            konto.auszahlen(Decimal("-100.00"))

        # - Auszahlung von ungültigem Typ → Exception?
        with pytest.raises(Auszahlungsfehler): 
            konto.auszahlen("Hello!")


class TestKontoGrenzfaelle:

    def test_placeholder_grenzfaelle(self):
        startbetrag = Decimal("100.00")
        einzahlungsbetrag_gross = Decimal("10_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000.00") # 1 Googol 10^100
        einzahlungsbetrag_klein = Decimal("0.00123")
        konto1 = Konto(1, startbetrag)
        konto2 = Konto(2, startbetrag)
        konto3 = Konto(3, einzahlungsbetrag_klein)
        konto4 = Konto(4, startbetrag)
        konto5 = Konto(4, startbetrag)
        konto6 = Konto(5, startbetrag)
        konto7 = Konto(4, startbetrag + Decimal("0.01"))

        # - Sehr kleine Beträge (Cent-Bereich)
        konto1.einzahlen(einzahlungsbetrag_klein)
        assert konto1.saldo == startbetrag # ich erwarte 100.00 + 0.00123 == 100.00

        # - Sehr große Beträge
        konto2.einzahlen(einzahlungsbetrag_gross)
        assert konto2.saldo == startbetrag + einzahlungsbetrag_gross

        # - Decimal-Präzision
        assert konto3.saldo != einzahlungsbetrag_klein # ich erwarte 0.00, nicht 0.00123 

        # - String-Repräsentation (__str__, __repr__)
        str_result = print(konto6)
        repr_result = repr(konto6)

        assert "Konto-ID: 5 Saldo: 100.00" in str_result 
        assert "Konto-ID: 5 Saldo: 100.00" in repr_result 
        
        # - Gleichheit von Konten
        assert konto4 == konto5
        assert konto4 != konto6
        assert konto4 != konto7