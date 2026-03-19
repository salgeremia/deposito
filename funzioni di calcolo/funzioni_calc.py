l = [5, 6, 7, 6, 3, 8, 4]

# Funzioni statistiche
# 1. Calcolare il massimo/minimo
massimo = max(l)
minimo = min(l)
print("Il valore massimo è", massimo)
print("Il valore minimo è", minimo)

# 2. Calcolare la media aritmetica
'''Per calcolare la media devo:
    - sommare gli elementi della lista
    - dividere per il numero di elementi
'''
somma = sum(l)
numero_valori = len(l)
media = somma/numero_valori
print("La media dei valori è:", media)

# 3. Conta quanti valori della lista sono uguali a zero
lista = [0, 1, 1, 0, 1, 1, 0]
conta = 0
for elemento in lista:
    if elemento == 0:
        conta += 1
print("Sono presenti", conta, "zeri")

# Funzioni matematiche
# 1. Calcolare la potenza di un numero
base = 5
esponente = 3
potenza = base ** esponente
print(base, "elevato alla", esponente, "è:", potenza)

# 2. Calcolare la radice quadrata di un numero
n = 81
radice = n ** 0.5
print("La radice quadrata di", n, "è:", radice)

# Funzioni logiche
# 1. Verifica se la condizione è vera o falsa
temperatura = 17
if temperatura < 15:
    print("Freddo!")
else:
    print("Caldo!")
