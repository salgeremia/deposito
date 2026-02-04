# Stampa le seguenti forme:

# task 1: stampa a video un quadrato di dimensione nxn
'''
 _ _ _ _ 
|       |
|       |
|       |
|_ _ _ _|
'''
n = 4
print(' _' * n)
for _ in range(n-1):
    print('|', ' ' * (2*n-1), '|', sep='')
print('|', '_ ' * (n-1), '_|', sep='')

# task 2: stampa a video un rettangolo di dimensione nxm
'''
 _ _ _ _ 
|       |
|       |
|_ _ _ _|
'''
m = 3
print(' _' * n)
for _ in range(m-1):
    print('|', ' ' * (2*n-1), '|', sep='')
print('|', '_ ' * (n-1), '_|', sep='')

# task 3: stampa a video un triangolo isoscele di base n
''' 
   /\
  /  \
 /    \
/______\
'''