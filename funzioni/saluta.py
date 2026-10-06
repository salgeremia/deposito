# Definisco la procedura 'saluta'
def saluta():
    print('Ciao')
# NOTA BENE: 'saluta' è una procedura poiché non restituisce valori

def saluta_persona(nome):
    print(f'Ciao {nome}, benvenut@ alla lezione sulle funzioni/procedure.')
# 'nome' è il parametro formale della procedura 'saluta_persona'

# Definisco la funzione 'get_anno_corrente'
def get_anno_corrente():
    return 2026
# la funzione 'get_anno_corrente' restituisce il valore l'anno corrente, 2026


# Invoco la procedura 'saluta'
saluta()
# Invoco la procedura 'saluta_persona'
saluta_persona('Alessandro')
saluta_persona('Camilla')
# Invoco la funzione 'get_anno_corrente'
anno = get_anno_corrente()
print('Siamo nel', anno)
