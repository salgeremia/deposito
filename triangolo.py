'''
Scrivi un programma che chieda all’utente le misure dei lati di un triangolo 
e calcoli area e perimetro. Il programma si compone delle funzioni:
1. misure_valide: restituisce True se le misure dei lati sono valide, 
    altrimenti restituisce False;
2. perimetro: restituisce la somma dei lati del triangolo;
3. area: restituisce l’area del triangolo calcolata con la formula di Erone.
_____________________________________________________
- DISUGUAGLIANZA TRIANGOLARE: ogni lato è minore della somma degli altri due.
- FORMULA DI ERONE: area = √(p x (p-a) x (p-b) x (p-c))
dove a, b, c sono le misure dei lati e p è il semiperimetro.
- RADICE QUADRATA: √x = math.sqrt(x), inserendo import math ad inizio codice.
'''
import math

def misure_valide(a, b, c):
    if a < b+c and b < a+c and c < a+b:
        return True
    else:
        return False

def perimetro(a, b, c):
    if misure_valide(a, b, c):
        return a+b+c
    else:
        return 0

def area(a, b, c):
    p = perimetro(a, b, c)/2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))

a, b, c = 3, 4, 5
print(area(a, b, c))
