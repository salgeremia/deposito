import turtle as t

t.speed(0)

ampiezza = int(input('Inserire passo: '))
# Disegno l'inviluppo di parabola
t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor('yellow')
for i in range(1, 300//ampiezza + 1):
    distanza = ampiezza * i
    t.goto(distanza, 0)
    t.penup()
    t.goto(0, 300-distanza)
    t.pendown()

t.penup()
t.goto(0, 300)
t.pendown()
t.pencolor('green')
for i in range(1, 300//ampiezza + 1):
    distanza = ampiezza * i
    t.goto(-distanza, 0)
    t.penup()
    t.goto(0, 300-distanza)
    t.pendown()

t.penup()
t.goto(0, -300)
t.pendown()
t.pencolor('blue')
for i in range(1, 300//ampiezza + 1):
    distanza = ampiezza * i
    t.goto(-distanza, 0)
    t.penup()
    t.goto(0, -300+distanza)
    t.pendown()

t.penup()
t.goto(0, -300)
t.pendown()
t.pencolor('orange')
for i in range(1, 300//ampiezza + 1):
    distanza = ampiezza * i
    t.goto(distanza, 0)
    t.penup()
    t.goto(0, -300+distanza)
    t.pendown()

t.hideturtle()
t.done()

