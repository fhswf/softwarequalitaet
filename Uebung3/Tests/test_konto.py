"""
CRVA
Test-Template für die Konto-Klasse (Test-After Approach)
========================================================
"""

import pytest
from decimal import Decimal
from Uebung3.Code.konto import Konto, Kontofehler, Einzahlungsfehler, Auszahlungsfehler


class TestKontoErstellung:
    """
    Testet die Kontoerstellung
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
        with pytest.raises(Kontofehler):
            konto = Konto(-1, Decimal("0.00"))

        with pytest.raises(Kontofehler):
            konto = Konto("Hello", Decimal("0.00"))

        with pytest.raises(Kontofehler):
            konto = Konto(-123, Decimal("0.00"))

        # Konto mit ungültigem Saldo (negativ, String) → Exception?
        with pytest.raises(Kontofehler):
            konto = Konto(3, Decimal("-50.45"))

        with pytest.raises(Kontofehler):
            konto = Konto(4, "Hello!")


class TestKontoEigenschaften:
    """
    Testet die Eigenschaften von konto.Konto
    """

    def test_placeholder_eigenschaften(self):
        test_id = 1
        startsaldo = Decimal("100.00")
        konto = Konto(test_id, startsaldo)
        
        # - konto.konto_id gibt korrekte ID zurück
        assert konto.konto_id == test_id

        # - konto.saldo gibt korrekten Saldo zurück
        assert konto.saldo == startsaldo
        
        # - Properties sind read-only (falls gewünscht)
        with pytest.raises(AttributeError): 
            konto.konto_id = 10

        with pytest.raises(AttributeError): 
            konto.saldo = Decimal("12.13")
        

class TestEinzahlung:
    """
    Testet den korrekten Ablauf von Einzahlungen
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
    """
    Testet den korrekten Ablauf von Auszahlungen
    """

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
    """
    Testet Grenzfälle: Große Zahlen oder Zahlen < 0.01 (Zinsen?), sowie String-Repräsentation
    """

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
        str_result = str(konto6)
        repr_result = repr(konto6)

        assert "Konto-ID: 5 Saldo: 100.00" in str_result 
        assert "Konto-ID: 5 Saldo: 100.00" in repr_result 
        
        # - Gleichheit von Konten
        assert konto4 == konto5
        assert konto4 != konto6
        assert konto4 != konto7