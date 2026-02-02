'''
Task 2
Crea un nuovo programma (file verifica.py) all'interno del quale è presente l'import della classe 
(es. from binary_search_tree import BinarySearchTree).

In questo programma vengono generati 100 numeri casuali interi, compresi nell'intervallo chiuso [0, 99] 
ed inseriti in un BST.
'''

from binary_search_tree import BinarySearchTree
import random

tree = BinarySearchTree()
for _ in range(100):
    tree.insert(random.randint(0, 99))


'''
Task 3
Ti viene chiesto di implementare una nuova classe: BinarySearchTree_124.

Il "124" non rimanda al modello dell'autovettura prodotta dalla FIAT tra gli anni 60 e 70 
dello scorso secolo, bensì al numero massimo di elementi che l'albero può contenere. 

Sulla base del codice presente nella classe BinarySearchTree (quello originale), quale o quali metodi 
modificheresti per soddisfare la richiesta?
'''
class BinarySearchTree_124(BinarySearchTree):
    def __init__(self) -> None:
        super().__init__()

    def insert(self, value: int) -> None:
        if self.size() < 4:
            if self.value is None:
                self.value = value
                self.left = BinarySearchTree_124()
                self.right = BinarySearchTree_124()
            else:
                if value < self.value:
                    self.left.insert(value)     # type: ignore
                else:
                    self.right.insert(value)    # type: ignore
        else:
            print('Albero pieno!')

    def size(self):
        if self.value is None:
            return 0 
        else: 
            return 1 + self.left.size() + self.right.size()


if __name__ == "__main__":
    tree = BinarySearchTree_124()
    tree.insert(8)
    tree.insert(4)
    tree.insert(10)
    tree.insert(9)
    print(tree)
    tree.insert(5)
    print(tree)
    