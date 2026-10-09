def caratteri_singoli(stringa):
    for carattere in stringa:
        print(carattere)

def convertitore(stringa):
    for carattere in stringa:
        print(carattere, ord(carattere))

def converti_vocali(stringa):
    s = ''
    for carattere in stringa:
        if carattere in 'AEIOUaeiou':
            s += str(ord(carattere))
        else:
            s += carattere
    return s


s = 'Nel mezzo del cammin di nostra vita...'
s = 'enoteca'
#    0123456
 