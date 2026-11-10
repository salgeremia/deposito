# y = x**3 - x**2 - x + 2

# INTERVALLO
a, b = -2, 2
# Dobbiamo capire se la funzione cambia segno nell'intervallo (a, b)
f_a = a**3 - a**2 - a + 2
f_b = b**3 - b**2 - b + 2
if f_a * f_b < 0:
    m = (a + b)/2
    f_m = m**3 - m**2 - m + 2
    
    if f_m < 0:
        if f_a < 0:
            a = m
        elif f_a > 0:
            b = m
    elif f_m > 0:
        if f_a < 0:
            b = m
        elif f_a > 0:
            a = m
    else:
        print(m)

else:
    print('Impossibile procedere')