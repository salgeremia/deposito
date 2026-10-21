import random as r

punti_interni = 0
punti_totali = 50_000_000

for _ in range(punti_totali):
    x, y = r.random(), r.random()
    if x**2 + y **2 <= 1:
        punti_interni += 1
print(punti_interni, punti_totali)
print('pi greco =', 4 * punti_interni/punti_totali)
