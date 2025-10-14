"""
Test-Template für die KontoService-Klasse (Test-After Approach)
===============================================================
CRVA

TODO: Team B - Implementieren Sie hier Ihre Tests NACH der KontoService-Implementierung!

Arbeitsablauf:
1. Implementieren Sie zuerst die KontoService-Klasse in Code/konto_service.py
2. Schreiben Sie dann hier umfassende Tests für Ihren Service
3. Testen Sie alle Service-Methoden gründlich
4. Dokumentieren Sie Ihre Autorschaft in den Tests

Tipps für Service-Tests:
- Nutzen Sie pytest fixtures für Setup/Teardown
- Testen Sie Integration zwischen Service und Konto-Klasse
- Testen Sie sowohl normale als auch Grenzfälle
- Testen Sie Validierungslogik im Service
"""

import pytest
from decimal import Decimal
from ..Code.konto_service import KontoService, Transaktionsfehler
from ..Code.konto import Konto, Kontofehler, Einzahlungsfehler, Auszahlungsfehler


class TestKontoServiceErstellung:
    """
    Tests für KontoService-Erstellung und Setup
    TODO: Team B - Testet Service-Initialisierung
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
        assert service.get_max_konto_id == erwarteter_int
        
        # - Konto wird zur internen Liste hinzugefügt
        assert len(service.konten_auflisten) == erwarteter_int

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
    TODO: Team B - Testet Saldo-Abfragen und -Berechnungen
    """

    def test_placeholder_gesamtsaldo(self):
        """TODO: Team B - Tests für gesamtsaldo()"""
        # Beispiel-Tests:
        # - Gesamtsaldo bei leerer Kontenliste (0)
        # - Gesamtsaldo mit einem Konto
        # - Gesamtsaldo mit mehreren Konten
        # - Korrekte Summe aller Salden
        assert True, "TODO: Tests für gesamtsaldo implementieren"


class TestUtilityFunktionen:
    """
    Tests für Hilfsfunktionen
    TODO: Team B - Testet ID-Verwaltung und Export-Funktionen
    """

    def test_placeholder_get_max_konto_id(self):
        """TODO: Team B - Tests für get_max_konto_id()"""
        # Beispiel-Tests:
        # - Erste ID ist 1
        # - IDs werden fortlaufend vergeben
        # - Keine doppelten IDs
        assert True, "TODO: Tests für get_max_konto_id implementieren"


class TestKontoServiceIntegration:
    """
    Integration-Tests zwischen Service und Konto-Klassen
    TODO: Team B - Testet das Zusammenspiel aller Komponenten
    """

    def test_placeholder_vollstaendiger_workflow(self):
        """TODO: Team B - Test für kompletten Workflow"""
        # Beispiel-Test:
        # 1. Service erstellen
        # 2. Mehrere Konten erstellen
        # 3. Einzahlungen durchführen
        # 4. Überweisungen durchführen
        # 5. Gesamtsaldo prüfen
        assert True, "TODO: Integration-Test implementieren"
