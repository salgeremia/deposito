def f(x):
    return x**3 - 3

def exist(a, b):
    return True if f(a)*f(b) < 0 else False
'''
    if f(a)*f(b) < 0:
        return True
    else:
        return False
'''

def m(a, b):
    return (a+b)/2


a = -5
b = 5

while abs(a-b) > 0.001:
    print(a, b)
    if exist(a, b):
        med = m(a, b)
        if exist(a, med):
            b = med
        elif exist(med, b):
            a = med
        else:
            print('Hai trovato lo zero ->', med)
            break

