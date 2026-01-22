# Esempio di utilizzo di ADT albero binario di ricerca

from binary_search_tree import BinarySearchTree
import random as r

tree = BinarySearchTree()
# n = int(input('Numero di valori da inserire nell\'albero: '))
print('Valori generati casualmente:')
valori = []
while len(valori) < 10:
    v = r.randint(1, 100)
    print(v, end=' ')
    if v%2 == 0:
        valori.append(v)
print('\nValori presenti nella lista:')
print(valori)
for valore in valori:
    tree.insert(valore)
print('\nValori contenuti, in ordine crescente, nell\'albero:')
print(tree)

# ---
'''
Potrei avere diversi vincoli o richieste specifiche quando lavoro con BST.
Esempio 1: nell'albero è possibile inserire solo valori pari, partendo da 20 valori casuali.
'''
# Risoluzione 1: modificare il metodo insert della classe BinarySearchTree
# Risoluzione 2: intervenire sul valore random generato in questo file
'''
Esempio 2: inserire nel BST 10 valori pari generati casualmente.
Esempio 3: individuare tutte le occorrenze di un certo valore k.
'''
