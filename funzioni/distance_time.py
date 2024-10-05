import doctest

VEL_LUCE = 299_792.458

def tempo(distanza):
    '''Restituisce il tempo (s) impiegato dalla luce per percorrere una certa distanza (km).
    >>> tempo(299792.458)
    1.0
    >>> tempo(0)
    0.0
    >>> tempo(-1)
    0
    '''
    return distanza/VEL_LUCE if distanza >= 0 else 0


test = doctest.testmod()
print(test)