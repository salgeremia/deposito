def linear_search(element_list: list[int], key: int) -> bool:
    for element in element_list:
        if element == key:
            return True
    else:
        return False


l = [4, 6, 2, 1, 9, 0, 7, 3]
k = 5
print(linear_search(l, k))