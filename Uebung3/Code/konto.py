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
        if not isinstance(konto_id, int) and konto_id > 0:
            raise TypeError("Konto-ID muss eine ganze Zahl > 0 sein.")
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
            raise Einzahlungsfehler("Betrag muss vom Typ Decimal sein.")
        if betrag <= Decimal('0.00'): 
            raise Einzahlungsfehler("Einzahlung kann nicht null oder negativ sein.")
        self._saldo += betrag 
        self._saldo = self._saldo.quantize(Decimal("0.01"))
    
    def auszahlen(self, betrag: Decimal) -> None:
        if not isinstance(betrag, Decimal):
            raise Auszahlungsfehler("Betrag muss vom Typ Decimal sein.")
        if betrag <= Decimal('0.00'): 
            raise Auszahlungsfehler("Auszahlungsbetrag kann nicht null oder negativ sein.")
        if self._saldo - betrag < Decimal('0.00'): 
            raise Auszahlungsfehler("Das Konto darf nicht überzogen werden.")
        self._saldo -= betrag
        self._saldo = self._saldo.quantize(Decimal("0.01"))
    
    ## checks for equality, uses _konto_id and _saldo
    def __eq__(self, other):
        if not isinstance(other, Konto):
            return NotImplemented
        return self._konto_id == other._konto_id and self._saldo == other._saldo

    def return_string(self) -> str:
        return f"Konto-ID: {self._konto_id} Saldo: {self._saldo}"

    def __str__(self):
        return self.return_string()
    
    def __repr__(self):
        return self.return_string()


class Kontofehler(Exception):
    """ Fehler im Kontosystem """

class Auszahlungsfehler(Kontofehler):
    """ Betrag kann nicht ausgezahlt werden """

class Einzahlungsfehler(Kontofehler):
    """ Betrag kann nicht eingezahlt werden """