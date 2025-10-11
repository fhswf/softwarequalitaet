"""
Hier sollen Sie Ihre Implementierung der Konto-Klasse erstellen.

TODO: Implementieren Sie die Konto-Klasse basierend auf dem KontoInterface
"""

from decimal import Decimal
from .interfaces import KontoInterface

class Konto(KontoInterface):
    """
    TODO: Implementieren Sie diese Klasse
    
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """
    
    konto_id: int
    saldo: Decimal

    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if konto_id is None:
            raise ValueError("Konto-ID darf nicht leer sein.")
        if not isinstance(konto_id, int):
            raise TypeError("Konto-ID muss eine ganze Zahl sein.")
        if saldo < Decimal('0.00'):
            raise ValueError("Startsaldo darf nicht negativ sein.")

        self.konto_id = konto_id
        self.saldo = saldo
    
    @property
    def konto_id(self) -> int:
        return self.konto_id
    
    @property
    def saldo(self) -> Decimal:
        return self.saldo
    
    def einzahlen(self, betrag: Decimal) -> None:
        if betrag < 0.00: 
            raise ValueError("Einzahlung kann nicht negativ sein.")
        self.saldo += betrag 
    
    def auszahlen(self, betrag: Decimal) -> None:
        if betrag < 0.00: 
            raise Auszahlungsfehler("Auszahlungsbetrag kann nicht negativ sein")
        if self.saldo - betrag < 0.00: 
            raise Auszahlungsfehler("Das konto darf nicht überzogen werden")
        self.saldo -= betrag
        
    

class Kontofehler(Exception):
    """ Fehler im Kontosystem """
    pass

class Auszahlungsfehler(Kontofehler):
    """ Betrag kann nicht ausgezahlt werden """
    pass