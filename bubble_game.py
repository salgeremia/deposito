import random

def print_balloons():
    print('|', ' '.join(balloons), '|', end='')

balloons = ['O']*10
bomb = random.randint(1,10)
popped = set()
alive = True

while len(popped) < 5:
    print_balloons()
    choice = int(input(' -> '))
    if choice not in popped:
        if choice == bomb:
            alive = False
            balloons[choice-1] = '*'
            print_balloons()
            print('\n\n*** GAME OVER ***')
            break
        popped.add(choice)
        balloons[choice-1] = '_'

if alive:
    print_balloons()
    print('\n\n>>>> You WIN! <<<<')
    print('Bomb position:', bomb)

