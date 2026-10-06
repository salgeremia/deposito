import random as r

def spin_dice(n_spins):
    o = [0]*6
    for _ in range(n_spins):
        num = r.randint(1, 6)
        o[num-1] += 1
    return o

def spin_two_dice(n_spins):
    o = [0]*11
    for _ in range(n_spins):
        a = r.randint(1, 6)
        b = r.randint(1, 6)
        s = a+b
        o[s-2] += 1
    return o


print(spin_dice(6000))