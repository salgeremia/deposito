# f(x) = 1/1 + 1/2 + 1/3 + ... + 1/n

def harmonic(n):
    '''Return the sum of the first n terms of the harmonic series.'''
    h = 0         
    for i in range(1, n+1):
        h += 1/i
    return h

# Esempio di utilizzo
f = harmonic(10)
print(f)
