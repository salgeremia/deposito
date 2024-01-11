import random

print(10*'o')                   # stampa palloncini
bomb = random.randint(1,10)     # genera la bomba
alive = True

for _ in range(5):              # per 5 volte...
    choice = int(input('Quale palloncino vuoi scoppiare? '))
    if choice == bomb:
        alive = False
        print('ESPLOSO!')
        break

if alive:                       # se il giocatore è ancora vivo
    print('HAI VINTO.')
    print('La BOMBA si trova in posizione', bomb)

