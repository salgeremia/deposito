'''
1. Classificazione triangolo
Chiedi all'utente tre lati di un triangolo: a, b, c. 
Determina se il triangolo è:
- Equilatero
- Isoscele
- Scaleno

NB: non è necessario verificare se i lati possono formare un triangolo.
'''
print('> inserire misure lati triangolo:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a == b and b == c:
    print('-> EQUILATERO')
elif a != b and b != c:
    print('-> SCALENO')
else:
    print('-> ISOSCELE')

# SOLUZIONE ALTERNATIVA (or)
if a == b and b == c:
    print('-> EQUILATERO')
elif a == b or a == c or b == c:
    print('-> ISOSCELE')
else:
    print('-> SCALENO')
