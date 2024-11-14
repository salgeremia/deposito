def merge(one: list[int], two: list[int]):
    result = list()
    i, j = 0, 0
    while i < len(one) and j < len(two):
        if one[i] < two[j]:
            result.append(one[i])
            i += 1
        else:
            result.append(two[j])
            j += 1
    
    if i == len(one):
        for e in two[j:]:
            result.append(e)
    
    if j == len(two):
        for e in one[i:]:
            result.append(e)

    return result


a = [2, 4, 6]
b = [1, 3, 5]
print(merge(a, b))