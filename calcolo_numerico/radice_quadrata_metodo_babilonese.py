'''n = 90
n_iterate = 10

x = n/2         # x_0
y = n/x         # y_0

for i in range(n_iterate):
    a = (x+y)/2
    print(a)
    x = a
    y = n/x
'''

n = 90
soglia = 0.0001
x = n/2
y = n/x

while True:
    a = (x+y)/2     # x_1
    print(a)

    x = a
    y = n/x
    n_a = (x+y)/2   # x_2
    if a - n_a < soglia:
        break

print(n_a)
print(f'√{n} = {n_a:.4f}')
