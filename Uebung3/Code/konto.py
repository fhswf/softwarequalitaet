from decimal import Decimal
from interfaces import KontoInterface

class Konto(KontoInterface):
    """
    Regeln:
    - ID wird bei Erstellung mitgegeben (numerisch, darf nicht leer sein)
    - Konto darf nicht überzogen werden (Saldo < 0)
    - Fehler bei inkorrekter Nutzung werfen
    """
    _konto_id: int
    _saldo: Decimal


    def __init__(self, konto_id: int, saldo: Decimal = Decimal('0.00')):
        if konto_id is None:
            raise ValueError("Konto-ID darf nicht leer sein.")
        if not isinstance(konto_id, int):
            raise TypeError("Konto-ID muss eine ganze Zahl sein.")
        if not isinstance(saldo, Decimal):
            raise TypeError("Saldo muss Typ Decimal sein.")
        if saldo < Decimal('0.00'):
            raise ValueError("Startsaldo darf nicht negativ sein.")

        self._konto_id = konto_id
        self._saldo = saldo
    
    @property
    def konto_id(self) -> int:
        return self._konto_id
    
    @property
    def saldo(self) -> Decimal:
        return self._saldo
    
    def einzahlen(self, betrag: Decimal) -> None:
        if not isinstance(betrag, Decimal):
            raise TypeError("Betrag muss vom Typ Decimal sein.")
        if betrag < Decimal('0.00'): 
            raise ValueError("Einzahlung kann nicht negativ sein.")
        self._saldo += betrag 
    
    def auszahlen(self, betrag: Decimal) -> None:
        if not isinstance(betrag, Decimal):
            raise TypeError("Betrag muss vom Typ Decimal sein.")
        if betrag < Decimal('0.00'): 
            raise Auszahlungsfehler("Auszahlungsbetrag kann nicht negativ sein.")
        if self._saldo - betrag < Decimal('0.00'): 
            raise Auszahlungsfehler("Das Konto darf nicht überzogen werden.")
        self._saldo -= betrag
        
    

class Kontofehler(Exception):
    """ Fehler im Kontosystem """


class Auszahlungsfehler(Kontofehler):
    """ Betrag kann nicht ausgezahlt werden """
