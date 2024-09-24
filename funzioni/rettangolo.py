def perimetro(base, altezza):
    return 2 * (base + altezza)

def area(base, altezza):
    return base * altezza

def diagonale(base, altezza):
    return (base**2 + altezza**2)**0.5

b, h = 4, 5
p = perimetro(b, h)
a = area(b, h)
d = diagonale(b, h)
print(p, a, d)