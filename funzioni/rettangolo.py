def perimetro(base, altezza):
    return 2 * (base + altezza)

def area(base, altezza):
    return base * altezza

def diagonale(base, altezza):
    return (base**2 + altezza**2)**0.5


# MAP -> https://realpython.com/python-map-function/
b, h = map(int, input().split())
p = perimetro(b, h)
a = area(b, h)
d = diagonale(b, h)
print(p, a, d)