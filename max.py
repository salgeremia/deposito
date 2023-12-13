print('Inserisci i valori alle variabili')
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))

if x > y:
    max = x if x > z else z
else:
    max = y if y > z else z

print(f'Il massimo è {max}')
doppio = 2 * max
print(f'Il doppio del massimo è {doppio}')