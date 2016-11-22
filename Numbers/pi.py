from decimal import *


def piN(N):
    if not isinstance(N, int) or N < 0: return
    pi = Decimal(0)
    for i in xrange(0, N):
        term1 = Decimal(1) / Decimal(pow(16, i))
        term2 = Decimal(4) / Decimal(8 * i + 1)
        term3 = Decimal(2) / Decimal(8 * i + 4)
        term4 = Decimal(1) / Decimal(8 * i + 5)
        term5 = Decimal(1) / Decimal(8 * i + 6)
        pi = pi + term1 * (term2 - term3 - term4 - term5)
    return pi.__float__()
