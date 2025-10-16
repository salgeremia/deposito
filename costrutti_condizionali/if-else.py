'''
1. Numero pari o dispari
Scrivi un programma che chieda all’utente un numero intero (variabile n) 
e visualizzi mediante un messaggio a video se è pari o dispari.
'''
n = int(input('> inserire un numero intero: '))
if n%2 == 0:
    print('-> NUMERO PARI')
else:
    print('-> NUMERO DISPARI')

'''
2. Maggiorenne o minorenne
Scrivi un programma che chieda all’utente la sua età (variabile e), 
successivamente stampi a video uno dei seguenti messaggi:
- "Puoi entrare" se ha almeno 18 anni,
- "Accesso negato" altrimenti.
'''
e = int(input('> inserire età: '))
if e >= 18:
    print('Puoi entrare')
else:
    print('Accesso negato')
