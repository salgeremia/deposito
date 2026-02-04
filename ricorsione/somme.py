def sommatoria(valore):
    '''Restituisce la somma dei valori interi positivi nell'intervallo [1, n]'''
    if valore == 0:
        return 0
    else:
        return valore + sommatoria(valore-1)


sommatoria(7)