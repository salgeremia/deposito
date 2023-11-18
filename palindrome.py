def num_palindromo():
    n = int(input())
    for i in range(1, n):
        print(i, end='')
    for i in range(n, 0, -1):
        print(i, end='')
    print()

def verifica_palindromo(testo):
    return True if testo == testo[::-1] else False

num_palindromo()
print(verifica_palindromo('osso'))