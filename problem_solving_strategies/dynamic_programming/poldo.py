import math

def panini(valori, i=0, precedente=math.inf):
    if i == len(valori):
        return 0
    elif precedente > valori[i]:
        mangia = 1 + panini(valori, i+1, valori[i])
        rifiuta = panini(valori, i+1, precedente)
        return max(mangia, rifiuta)
    else:
        return panini(valori, i+1, precedente)
    
menu = [389, 400, 399, 207, 155, 300, 112, 158]
print('#panini =', panini(menu))