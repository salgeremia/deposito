'''
Considero qualsiasi testo formato da caratteri
alfabetici (minuscoli o maiuscoli) e trasformo
il testo nel suo corrispondente codificato
mediante uno spostamento (offset).
Es.
> parola = 'calCIo' 
> offset = 1 
> calCIo -> dbmDJp
'''

text = 'hashTAGz'
print(text)
offset = 3
text = text.upper()

for char in text:
    plain = ord(char) - ord('A')    # 25
    plain = plain + offset          # 28
    plain = plain % 26              # 2
    plain = plain + ord('A')        # 67 
    print(chr(plain), end='')
print()
