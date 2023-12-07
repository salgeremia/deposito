esercizi = [9, 8, 11]
punteggio = sum(esercizi)

if punteggio < 18:
    voto = 'Insufficiente'
else:
    if punteggio <= 30:
        voto = punteggio
    elif punteggio > 30 and min(esercizi) >= 10:
        voto = '30 e LODE'
    else:
        voto = 30

print(f'{esercizi} -> {punteggio} = {voto}')
