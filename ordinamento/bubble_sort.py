def bubble_sort(v):
    j = 0
    while j < len(v)-1:
        i = 0
        while i < len(v)-1:
            if v[i] > v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i += 1
        # print(v)
        j += 1

l = [7, 6, 5, 4, 3]
bubble_sort(l)
