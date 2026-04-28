import random as r
import time 
# Creo password di sole lettere MAIUSCOLE di lunghezza 4

start_creazione_password=time.time()

lunghezza = 5
password = ''
for _ in range(lunghezza):
    password += chr(r.randint(65, 90))

print(password)

end_creazione_password=time.time()

# Implemento algoritmo a forza bruta
'''
Per indovinare la password devo partire da "AAAA" e arrivare a "ZZZZ"
'''

start_indovina_password=time.time()
tentativo = [65 for _ in range(lunghezza)] #'A'=chr(65) -> tentativo=['A','A','A','A']
# Devo trasformare in carattere e unire in una stringa

indice=lunghezza-1
while ''.join([chr(x) for x in tentativo]) != password:
    #''.join([chr(x) for x in tentativo]) partendo dall'interno stiamo trasformando ogni x(numero all'interno di tentativo) in carattere e successivamente, una volta trasformato in lettera andiamo ad utilizzare join che trasforma la nostra lista in stringa(inserisce uno spazio libero '' tra ogni lettera, ricompattando la stringa)
    tentativo[-1]+=1 #il nostro ultimo elemento deve sempre scorrere, non deve avere un valore fisso
    if 91 in tentativo:#appena arriviamo alla Z in qualsiasi indice il programma va a trasformare il 90 in 65(da Z ad A) e successivamente incrementa ogni indice fino ad arrivare alla password desiderata
        indice=tentativo.index(91)#consideriamo 91  e non 90 altrimenti saltiamo la lettera Z
        tentativo[indice]=65
        tentativo[indice-1]+=1
        
end_indovina_password=time.time()

print(f'La password è: {''.join([chr(x) for x in tentativo])} \nTempo di creazione della password: {end_creazione_password-start_creazione_password}\nTempo per indovinare la password: {end_indovina_password-start_indovina_password}\nTempo TOTALE: {end_indovina_password-start_creazione_password}')

