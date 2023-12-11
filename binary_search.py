l = [6, 2, 9, 4, 1, 8, 3, 5, 7]
k = 8                               # k -> chiave, elemento da cercare
l.sort() 
trovato = False

# inizializzo gli indici utili alla ricerca
i = 0                               # i -> indice sinistro
f = len(l) - 1                      # f -> indice destro

while i <= f:
    m = (i+f) // 2                  # m -> indice del valore centrale
    if k == l[m]:
        trovato = True
        break
    elif k < l[m]:
        f = m - 1
    else:
        i = m + 1
    
print(trovato)