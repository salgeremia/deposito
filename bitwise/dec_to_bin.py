# Convertire un numero intero decimale in binario
n = 56
bin = ''
while n > 0:
    resto = n%2
    bin = str(resto) + bin
    n = n//2
print(bin)