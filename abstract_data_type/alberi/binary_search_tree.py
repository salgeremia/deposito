class BinarySearchTree:
    def __init__(self) -> None:
        self.value = None
        self.left = None
        self.right = None

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
tree.insert(5)
tree.insert(3)
tree.insert(4)
tree.insert(8)