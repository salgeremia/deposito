'''
1
2   3
4   5   6
7   8   9   10
'''
n_righe = int(input('Inserisci il numero di righe: '))
valore = 1
for riga in range(1, n_righe+1):
    for colonna in range(riga):
        print(valore, end='\t')
        valore += 1
    print()