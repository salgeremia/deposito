s = input('Testo da cifrare: ')
k = int(input('Chiave di cifratura: '))

s_cifrata = ''

for carattere in s:
    if 'A' <= carattere <= 'Z' or 'a' <= carattere <= 'z':
        if carattere.isupper():
            offset = 65
        else:
            offset = 97
        s_cifrata += chr((ord(carattere) + k - offset) % 26 + offset)
    else:
        s_cifrata += carattere

print('Testo cifrato:', s_cifrata)