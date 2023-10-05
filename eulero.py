import math

e = 1
print('Calcolo il valore di e\n0 ->', e)
for n in range(1, 10):
    e += 1/math.factorial(n)
    print(n, '->', e)


print('\nValore calcolato dalla funzione\n', math.e, sep='')