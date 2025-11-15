from decimal import getcontext, ROUND_HALF_UP

# globale Decimal-Präzision anpassen
getcontext().prec = 200
getcontext().rounding = ROUND_HALF_UP