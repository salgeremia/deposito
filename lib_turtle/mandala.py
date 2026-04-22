import turtle as t

t.speed(0)


# ELICA = triangolo verde x 4
t.fillcolor('lightgreen')
t.begin_fill()
for i in range(4):
    for _ in range(3):
        t.forward(100)
        t.left(120)
    t.left(90)
t.end_fill()

# ESAGONO = triangolo arancione x 6
t.fillcolor('orange')
t.begin_fill()
for i in range(6):
    for _ in range(3):
        t.forward(50)
        t.left(120)
    t.left(60)
t.end_fill()

# CIRCONFERENZA = raggio 100
t.color('blue')
t.pensize(5)
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

t.hideturtle()

t.done()