import turtle as t

lato = 280
distanza = 40
colori = ["lightblue", "lightgreen", "green", "yellow", "orange", "red", "brown", "black"]
n_quadrati = lato // distanza 
t.speed(8)

for i in range(n_quadrati):
    
    t.color(colori[i])
    t.begin_fill()

    for _ in range(4):
        t.forward(lato)
        t.left(90)

    t.end_fill()

    t.penup()
    t.forward(distanza)
    t.pendown()

    lato -= distanza

t.done()