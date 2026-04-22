import turtle as t

t.speed(0)
distanza = 30

# Disegno le colonne
for i in range(10):
    t.goto(distanza * i, 300)
    t.penup()
    t.goto(distanza * (i+1), 0)
    t.pendown()

# Riposiziono la penna in (0, 0)
t.penup()
t.goto(0, 0)
t.pendown()

# Disegno le righe
t.goto(270, 0)
t.penup()
t.goto(0, 30)
t.pendown()

t.goto(270, 30)
t.penup()
t.goto(0, 60)
t.pendown()

t.done()

