from random import randint

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None

    def __str__(self) -> str:
        text = ''
        node = self.head
        while node:
            text += f'{node.value} -> '     # type: ignore
            node = node.next                # type: ignore
        return f'{text} None'
        
    def append(self, value) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node           # type: ignore
            self.tail = node


l_list = LinkedList()
l_list.append(7)
l_list.append(3)
print(l_list)