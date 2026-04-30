'''
1
2   4
3   6   9
4   8   12  16
...
10  20  30  40  ... 100
'''
for riga in range(1, 11):
    for colonna in range(1, riga+1):
        print(riga*colonna, end='\t')
    print()