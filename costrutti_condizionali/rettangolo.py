# START
# base, altezza, area: int

base = int(input('Inserire base: '))
altezza = int(input('Inserire altezza: '))

if base < 0:
    print('Il valore della base è errato.\nRiprova.')
    base = int(input('Inserire base: '))
area = base * altezza
print('Area rettangolo =', area)
# END