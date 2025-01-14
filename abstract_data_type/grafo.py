g = {'1': [2, 3, 4],
     '2': [3, 4],
     '3': [4],
     '4': []}

def swap(start, end):
    if str(start) in g.keys():
        if end in g[str(start)]:
            g[str(start)].remove(end)
            g[str(end)].append(start)

def check_path(path):
    for i in range(len(path) - 1):
        if str(path[i]) in g.keys():
            if path[i+1] not in g[str(path[i])]:
                return False
        else:
            return False
    return True


print(g)
swap(2, 4)
print(g)
swap(1, 2)
print(g)
swap(4, 2)
print(g)
swap(2, 3)
print(g)

p = [3, 2, 1, 4]
print(check_path(p))