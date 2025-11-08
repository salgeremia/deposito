'''
PROBLEMA: trovare il valore massimo calcolabile come prodotto di potenze.
Es. se n = 5, il massimo valore calcolabile è 4^5 * 3^2 * 1 = 9216
'''
def max_value(n: int) -> int:
    if n <= 2:
        return n
    elif n == 3:
        return 3**2
    else:
        return (n-1)**n * max_value(n-2)
    