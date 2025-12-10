class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None
        self.len = 0

    def __str__(self) -> str:
        text = ''
        node = self.head
        while node:
            text += f'{node.value} -> '                                 # type: ignore
            node = node.next                                            # type: ignore
        return f'{text}|'
        
    def append(self, value) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node                                       # type: ignore
            self.tail = node
        self.len += 1
    
    def insert(self, index: int, value) -> None:
        if index < 0 or index > self.len:
            raise IndexError('Index out of bounds')
        
        if index == self.len:
            self.append(value)
            return
        else:
            node = Node(value)
            if index == 0:
                node.next = self.head                                   # type: ignore
                self.head = node
            else:
                current_node = self.head
                for _ in range(index - 1):
                    current_node = current_node.next                    # type: ignore
                node.next = current_node.next                           # type: ignore
                current_node.next = node                                # type: ignore
            self.len += 1 

    def remove(self, index: int):
        if index < 0 or index > self.len:
            raise IndexError('Index out of bounds')

        if index == 0:
            self.head = self.head.next                                  # type: ignore
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next                        # type: ignore
            if current_node.next is None:                               # type: ignore                           
                self.tail = current_node
            else:
                current_node.next = current_node.next.next              # type: ignore
        self.len -= 1


l_list = LinkedList()
l_list.append(7)            # 7 -> |
l_list.append(3)            # 7 -> 3 -> |
l_list.append(5)            # 7 -> 3 -> 5 -> |
l_list.insert(1, 4)         # 7 -> 4 -> 3 -> 5 -> |
l_list.insert(0, 9)         # 9 -> 7 -> 4 -> 3 -> 5 -> |
# l_list.insert(8, 8)
l_list.insert(5, 8)         # 9 -> 7 -> 4 -> 3 -> 5 -> 8 -> |
l_list.remove(0)            # 7 -> 4 -> 3 -> 5 -> 8 -> |
l_list.remove(4)            # 7 -> 4 -> 3 -> 5 -> |
print(l_list)