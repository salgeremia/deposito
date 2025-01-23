# Scrivere un semplice codice per simulare un login con un massimo di 3 tentativi.
 
# DA FARE:
# 1. oscurare l'input dell'utente
# 2. inserire un timer di 30 secondi dopo il terzo tentativo

password_db = 'password'
tentativi = 3

while tentativi > 0:
    password_utente = input('Inserisci la password: ')
    if password_utente == password_db:
        print('Login effettuato con successo')
        break
    else:
        tentativi -= 1
        print(f'Password errata, tentativi rimasti: {tentativi}')

if tentativi == 0:
    print('Tentativi esauriti, riprova tra 30 secondi')
