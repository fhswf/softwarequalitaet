"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================
CRVA
"""

import pytest
from decimal import Decimal
from ..Code.konto_service import KontoService, Transaktionsfehler
from ..Code.konto import Kontofehler, Einzahlungsfehler, Auszahlungsfehler


class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    """

    def test_placeholder_service_erstellung(self):
        service = KontoService()
        assert len(service.konten_auflisten()) == 0


class TestKontoVerwaltung:
    """
    Tests für Konto-Erstellung und -Verwaltung
    """

    def test_placeholder_konto_erstellen(self):
        service = KontoService()
        startgesamtsaldo = Decimal("100.00")
        erwarteter_int = 1

        # - Rückgabe der Konto-ID
        assert service.konto_erstellen(startgesamtsaldo) == erwarteter_int
        
        # - Konto mit gültigem Saldo erstellen
        assert service.gesamtsaldo_berechnen() == startgesamtsaldo
        
        # - Konto-ID wird automatisch vergeben
        assert service.get_max_konto_id() == erwarteter_int
        
        # - Konto wird zur internen Liste hinzugefügt
        assert len(service.konten_auflisten()) == erwarteter_int

        # - Erstellen mit ungültigem Saldo → Exception?
        with pytest.raises(Kontofehler):
            service.konto_erstellen(Decimal("-50.00"))

        with pytest.raises(Kontofehler):
            service.konto_erstellen("Hello!")
        

    def test_placeholder_konten_auflisten(self):
        service = KontoService()
        startgesamtsaldo = Decimal("100.00")
        erwarteter_int_vor = 0
        erwarteter_int_nach = 1
        
        # - Leere Liste bei Service-Start
        assert len(service.konten_auflisten()) == erwarteter_int_vor
        
        # - Liste nach Konto-Erstellung
        service.konto_erstellen(startgesamtsaldo)
        assert len(service.konten_auflisten()) == erwarteter_int_nach

        # - Korrekte Anzahl und Inhalte
        test_arr = service.konten_auflisten()
        assert "konto_id" in test_arr[0] and test_arr[0]["konto_id"] == erwarteter_int_nach and "saldo" in test_arr[0] and test_arr[0]["saldo"] == startgesamtsaldo


class TestTransaktionen:
    """
    Tests für Transaktions-Funktionen
    """

    def test_placeholder_einzahlen(self):
        konto_service = KontoService()
        einzahlungsbetrag = Decimal("100.00")
        einzahlungsbetrag_ungueltig = "Hallo!"
        gueltige_konto_id = 1
        ungueltige_konto_id = 2
        konto_service.konto_erstellen(einzahlungsbetrag)

        # - Einzahlung auf existierendes Konto
        # - Saldo wird korrekt erhöht
        konto_service.einzahlen(gueltige_konto_id, einzahlungsbetrag)
        assert konto_service.gesamtsaldo_berechnen() == einzahlungsbetrag + einzahlungsbetrag

        # - Einzahlung auf nicht-existierendes Konto → Exception?
        with pytest.raises(Transaktionsfehler):
            konto_service.einzahlen(ungueltige_konto_id, einzahlungsbetrag)

        # - Ungültiger Betrag → Exception?
        with pytest.raises(Einzahlungsfehler):
            konto_service.einzahlen(gueltige_konto_id, einzahlungsbetrag_ungueltig)

    def test_placeholder_auszahlen(self):
        konto_service = KontoService()
        auszahlungsbetrag = Decimal("100.00")
        erwarteter_gesamtsaldo = Decimal("0.00")
        gueltige_konto_id = 1
        ungueltige_konto_id = 2
        konto_service.konto_erstellen(auszahlungsbetrag)
        
        # - Auszahlung bei ausreichendem Saldo
        # - Saldo wird korrekt reduziert
        konto_service.auszahlen(gueltige_konto_id, auszahlungsbetrag)
        assert konto_service.gesamtsaldo_berechnen() == erwarteter_gesamtsaldo
                
        # - Auszahlung bei unzureichendem Saldo → Exception?
        with pytest.raises(Auszahlungsfehler):
            konto_service.auszahlen(gueltige_konto_id, auszahlungsbetrag)

        # - Auszahlung von nicht-existierendem Konto → Exception?
        with pytest.raises(Transaktionsfehler):
            konto_service.auszahlen(ungueltige_konto_id, auszahlungsbetrag)

    def test_placeholder_ueberweisen(self):
        konto_service = KontoService()
        betrag = Decimal("100.00")
        erwarteter_gesamtsaldo = Decimal("200.00")
        erwarteter_sendersaldo = Decimal("0.00")
        gueltige_konto_id_1 = 1
        gueltige_konto_id_2 = 2
        ungueltige_konto_id = 3
        konto_service.konto_erstellen(betrag)
        konto_service.konto_erstellen(betrag)

        # - Überweisung zwischen existierenden Konten
        konto_service.ueberweisen(gueltige_konto_id_1, gueltige_konto_id_2, betrag)
        assert konto_service.gesamtsaldo_berechnen() == erwarteter_gesamtsaldo

        liste = konto_service.konten_auflisten()
        # - Sender-Saldo wird reduziert
        assert liste[0]["saldo"] == erwarteter_sendersaldo
        
        # - Empfänger-Saldo wird erhöht
        assert liste[1]["saldo"] == erwarteter_gesamtsaldo

        # - Überweisung bei unzureichendem Saldo → Exception?
        with pytest.raises(Auszahlungsfehler):
            konto_service.ueberweisen(gueltige_konto_id_1, gueltige_konto_id_2, betrag)

        # - Überweisung an nicht-existierendes Konto → Exception?
        with pytest.raises(Transaktionsfehler):
            konto_service.ueberweisen(gueltige_konto_id_1, ungueltige_konto_id, betrag)

        # - Überweisung von nicht-existierendem Konto → Exception?
        with pytest.raises(Transaktionsfehler):
            konto_service.ueberweisen(ungueltige_konto_id, gueltige_konto_id_2, betrag)


class TestSaldoFunktionen:
    """
    Tests für Saldo-bezogene Funktionen
    """

    def test_placeholder_gesamtsaldo(self):
        konto_service = KontoService()
        betrag = Decimal("100.00")
        erwarteter_gesamtsaldo = Decimal("0.00")

        # - Gesamtsaldo bei leerer Kontenliste (0)
        assert konto_service.gesamtsaldo_berechnen() == erwarteter_gesamtsaldo

        # - Gesamtsaldo mit einem Konto
        konto_service.konto_erstellen(betrag)
        assert konto_service.gesamtsaldo_berechnen() == betrag

        # - Gesamtsaldo mit mehreren Konten
        konto_service.konto_erstellen(betrag)
        assert konto_service.gesamtsaldo_berechnen() == betrag + betrag


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    """

    def test_placeholder_get_max_konto_id(self):
        konto_service = KontoService()
        betrag: Decimal = Decimal("100.00")
        erwartete_erste_id = 1
        erwartete_letzte_id = 1000

        # - Erste ID ist 1
        # - IDs werden fortlaufend vergeben
        for i in range(erwartete_erste_id, erwartete_letzte_id + 1): 
            assert konto_service.konto_erstellen(betrag) == i
            if i == erwartete_letzte_id: 
                assert konto_service.get_max_konto_id() == erwartete_letzte_id

        # - Keine doppelten IDs
        kontenliste = konto_service.konten_auflisten()
        for i in range(erwartete_erste_id, erwartete_letzte_id + 1):
            count_for_i = 0
            for k in kontenliste:
                if k["konto_id"] == i: 
                    count_for_i += 1
            assert count_for_i == 1


class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    """

    def test_placeholder_vollstaendiger_workflow(self):
        betrag: Decimal = Decimal("100.00")
        erwartetes_gesamtsaldo = Decimal("700.00")
        erwartete_erste_id = 1
        erwartete_letzte_id = 5
        
        # 1. Service erstellen
        konto_service = KontoService()
        assert konto_service

        # 2. Mehrere Konten erstellen
        for i in range(erwartete_erste_id, erwartete_letzte_id + 1): 
            assert konto_service.konto_erstellen(betrag) == i
            if i == erwartete_letzte_id: 
                assert konto_service.get_max_konto_id() == erwartete_letzte_id

        # 3. Einzahlungen durchführen
        konto_service.einzahlen(4, betrag)
        konto_service.einzahlen(5, betrag)
        assert konto_service.gesamtsaldo_berechnen() == erwartetes_gesamtsaldo

        # 4. Überweisungen durchführen
        konto_service.ueberweisen(4, 5, betrag)
        konto_service.ueberweisen(1, 5, betrag)
        with pytest.raises(Transaktionsfehler):
            konto_service.ueberweisen(3, 5, betrag + betrag)

        # 5. Gesamtsaldo prüfen
        assert konto_service.gesamtsaldo_berechnen() == erwartetes_gesamtsaldo
