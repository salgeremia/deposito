from time import process_time

def somma_for(lista):
    s = 0
    for elemento in lista:
        s += elemento
    return s

def somma_while(lista):
    s, i = 0, 0
    while i < len(lista):
        s += lista[i]
        i += 1
    return s


l = [1]*1_000_000

t_inizale = process_time()
s = sum(l)
t_totale = process_time() - t_inizale
print(f'sum:\t{s} -> {t_totale}')

t_inizale = process_time()
s = somma_for(l)
t_totale = process_time() - t_inizale
print(f'for:\t{s} -> {t_totale}')

t_inizale = process_time()
s = somma_while(l)
t_totale = process_time() - t_inizale
print(f'while:\t{s} -> {t_totale}')
