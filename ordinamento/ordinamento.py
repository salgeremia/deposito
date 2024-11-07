def insertion_sort(vector):
    for i in range(1, len(vector)):
        k = vector[i]
        p = i - 1
        while vector[p] > k and p >= 0:
            vector[p+1] = vector[p]
            p -= 1
        vector[p+1] = k        
    return vector


v = [5, 2, 7, 3]
print(insertion_sort(v))