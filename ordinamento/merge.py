def merge(left: list[int], right: list[int]):
    result = list()
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left):
        for e in right[j:]:
            result.append(e)

    elif j == len(right):
        for e in left[i:]:
            result.append(e)
    return result

def merge_sort(v: list[int]):
    if len(v) > 1:
        med = len(v) // 2
        l = v[:med]
        r = v[med:]
        print(l, r)
        sorted_left = merge_sort(l)
        sorted_right = merge_sort(r)
        return merge(sorted_left, sorted_right)
    else:
        return v


x = [5, 1, 4, 3]
print(merge_sort(x))