'''
Realizza la procedura bonus che si comporta nel seguente modo:
bonus("testo")
> t         1
> es        2-3
> sto       3-4-5
> to        4-5
> o         5
'''

def bonus(testo):
    fine = 1
    for i in range(len(testo)):
        print(testo[i:(fine+i)])
        fine += 1

bonus('testo')