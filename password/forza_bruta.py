import random as r

# Creo password di sole lettere MAIUSCOLE di lunghezza 4
lunghezza = 4
password = ''
for _ in range(lunghezza):
    password += chr(r.randint(65, 90))

print(password)

# Implemento algoritmo a forza bruta
'''
Per indovinare la password devo partire da "AAAA" e arrivare a "ZZZZ"
'''
tentativo = [65, 65, 65, 65]
# Devo trasformare in carattere e unire in una stringa
while tentativo != password: