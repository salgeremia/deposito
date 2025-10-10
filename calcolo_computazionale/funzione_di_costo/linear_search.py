# Calcolo della funzione di costo T(n)

# ALGORITMO DI RICERCA LINEARE
def linear_search(v, value):    # WORSE     BEST        MEDIUM
    found = False               # 1         1           1
    i = 0                       # 1         1           1
    while i < len(v):           # n + 1     n + 1       n + 1
        if v[i] == value:       # n         n           n
            found = True        # n         0           n/2
        i += 1                  # n         n           n
    return found                # 1         1           1
                                # _____     _____       _____
# FUNZIONE DI COSTO        T(n) = 4n + 4    3n + 4      3n + 1/2n + 4 = 7/2n + 4

# ALGORITMO DI RICERCA LINEARE CON SENTINELLA
def sentinel_linear_search(v, value):
    i = 0                       # 1         1             
    while i < len(v):           # n + 1     1           
        if v[i] == value:       # n         1           
            return True         # 0         1           
        i += 1                  # n         0           
    return False                # 1         0           
                                # _____     _____       _____
# FUNZIONE DI COSTO        T(n) = 3n + 3    4           

