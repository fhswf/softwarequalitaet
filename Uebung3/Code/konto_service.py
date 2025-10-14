from decimal import Decimal
from typing import List, Dict
from .interfaces import KontoServiceInterface, KontoInterface
from .konto import Konto

class KontoService(KontoServiceInterface):
    """
    Funktionalitäten:
    - Konten verwalten (als List[KontoInterface])
    - Validierung der Benutzereingaben
    - Neue KontoID: max KontoID + 1
    - Export-Funktionen
    - Berechnungen
    """

    def __init__(self):
        self._konten: List[KontoInterface] = []

    def _create_konto(self, konto_id: int, saldo: Decimal) -> KontoInterface:
        return Konto(konto_id, saldo)

    def konten_auflisten(self) -> List[Dict]:
        result: List[Dict] = []
        for konto in self._konten: 
            result.append({"konto_id": konto.konto_id, "saldo": konto.saldo})
        return result
 
    def konto_erstellen(self, saldo: Decimal = Decimal('0.00')) -> int:
        konto_id = self.get_max_konto_id() + 1
        konto = self._create_konto(konto_id, saldo)
        self._konten.append(konto)
        return konto_id

    # to transfer money to someone else
    def ueberweisen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        konto_von: KontoInterface = self.__get_konto_by_id(von_konto_id)
        konto_zu: KontoInterface = self.__get_konto_by_id(zu_konto_id)
        konto_von.auszahlen(betrag) # this order, because if auszahlen() fails, it will raise an error and konto_zu remains untouched
        konto_zu.einzahlen(betrag)

    # to 'grab' money from the konto of someone else
    def einziehen(self, von_konto_id: int, zu_konto_id: int, betrag: Decimal) -> None:
        konto_von: KontoInterface = self.__get_konto_by_id(von_konto_id)
        konto_zu: KontoInterface = self.__get_konto_by_id(zu_konto_id)
        konto_zu.auszahlen(betrag) # this order, because if auszahlen() fails, it will raise an error and konto_von remains untouched
        konto_von.einzahlen(betrag)
    
    # added because of test's requirement
    def einzahlen(self, konto_id: int, betrag: Decimal) -> None: 
        konto_zu: KontoInterface = self.__get_konto_by_id(konto_id)
        konto_zu.einzahlen(betrag)
    
    # added because of test's requirement
    def auszahlen(self, konto_id: int, betrag: Decimal) -> None:
        konto_von: KontoInterface = self.__get_konto_by_id(konto_id)
        konto_von.auszahlen(betrag)
        

    def get_max_konto_id(self) -> int:
        if not self._konten:
            return 0
        return max(k.konto_id for k in self._konten)

    def gesamtsaldo_berechnen(self) -> Decimal:
        summe: Decimal = Decimal('0.00')
        for konto in self._konten:
            summe += konto.saldo
        return summe

    # private helper func, use only within this class!
    # ensures, that we got the right konto, if _konten ever gets shuffled
    # raises exception if the konto was not found
    def __get_konto_by_id(self, konto_id: int) -> KontoInterface: 
        for konto in self._konten:
            if konto.konto_id == konto_id: 
                return konto
        raise Transaktionsfehler(f"Konto mit der ID {konto_id} wurde nicht gefunden.")
    



    
class Transaktionsfehler(Exception):
    """Fehler bei Transaktion"""