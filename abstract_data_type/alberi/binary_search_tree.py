class BinarySearchTree:
    def __init__(self) -> None:
        self.value = None
        self.left = None
        self.right = None

    def __str__(self) -> str:
        if self.value is None:
            return ''
        else:
            return f'{self.left} {self.value} {self.right}'

    def __contains__(self, value: int) -> bool:
        if self.value is None:
            return False
        elif self.value == value:
            return True
        elif value < self.value:
            return self.left.__contains__(value)       # type: ignore
        else:
            return self.right.__contains__(value)      # type: ignore
        
    def insert(self, value: int) -> None:
        if self.value is None:
            self.value = value
            self.left = BinarySearchTree()
            self.right = BinarySearchTree()
        else:
            if value < self.value:
                self.left.insert(value)     # type: ignore
            else:
                self.right.insert(value)    # type: ignore  


tree = BinarySearchTree()
tree.insert(6)
tree.insert(4)
tree.insert(2)
tree.insert(8)
tree.insert(5)
tree.insert(7)
print(tree.__contains__(8))
print(tree)