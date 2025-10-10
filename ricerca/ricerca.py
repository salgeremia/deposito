def linear_search(elements_list: list[int], key: int) -> bool:
    for element in elements_list:
        if element == key:
            return True
    return False

def binary_search(elements_list: list[int], key: int) -> bool:
    found = False
    element = elements_list[len(elements_list) // 2 - 1]
    if len(elements_list) > 1
    if element == key:
        return True
    
    elif element > key:




l = [4, 6, 2, 1, 9, 0, 7, 3]
k = 5
print(linear_search(l, k))
print(binary_search(sorted(l), k))