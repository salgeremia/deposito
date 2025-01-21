'''
Formula di Eulero:
π = √(6x)

x1 = 1/1**2
x2 = x1 + 1/2**2
x3 = x2 + 1/3**2
...
x_(i) = x_(i-1) + 1/i**2
'''

def pi_definito(n_iterate):
    x = 0
    for i in range(1, n_iterate + 1):
        # print(f'\nx = {x} + 1/{i}^2 = ', end='')
        x += 1/i**2
        # print(x)
        pi = (6 * x)**0.5
        # print(f'π = {pi}')
    return pi


def pi_indefinito(soglia):
    i = 1
    x = 1
    pi_old = 6**0.5
    # print(f'{i} -> {pi_old}')
    while True:
        i += 1
        x += 1/i**2
        pi = (6 * x)**0.5
        # print(f'{i} -> {pi}')
        if pi - pi_old <= soglia:
            return pi
        pi_old = pi


print(pi_definito(978))
print(pi_indefinito(0.000001))