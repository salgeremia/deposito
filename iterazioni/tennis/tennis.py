p = 0
d = 0
c = 0
b = 0
while True:
    n = int(input())
    if p != 40 or d != 40:
        if n == 1:
            if c == 2:
                p += 10
            else:
                p += 15
                c += 1
        else:
            if b == 2:
                d+= 10
            else:
                d += 15
    else:
        if p == 40:
            print("Vince giocatore 1")
            break
    if p== 40 and d == 40:
        if n == 1:
            print("Vantaggio giocatore 1")
            c += 1
            break
        else:
            print("Vantaggio giocatore 2")
            b += 1
            break
        if c == 4:
            print("Fine del game. ha vinto il giocatore 1")
        if b == 4:
            print("Fine del game ha vinto il giocatore 2")