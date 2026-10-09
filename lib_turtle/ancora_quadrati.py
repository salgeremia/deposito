import turtle as t

n = int(input('n = '))
t.speed(0)

lato = 5
t.penup()
t.goto(-300, 300)
t.pendown()
# for i in range(n):
#     # disegna quadrato
#     for _ in range(4):
#         t.forward(lato)
#         t.left(90)
#     # riposiziono la penna sul vertice in basso a sinistra del prossimo quadrato
#     t.penup()
#     t.forward(lato)
#     t.right(90)
#     lato *= 2
#     t.forward(lato)
#     t.left(90)
#     t.pendown()

colori = ['lightblue', 'lightgreen', 'yellow']
# for i in range(n):
#     t.color(colori[i%3])
#     t.begin_fill()
#     # disegna quadrato
#     for _ in range(4):
#         t.forward(lato)
#         t.left(90)
#     t.end_fill()
#     # riposiziono la penna sul vertice in basso a sinistra del prossimo quadrato
#     t.penup()
#     t.forward(lato)
#     t.right(90)
#     lato *= 2
#     t.forward(lato)
#     t.left(90)
#     t.pendown()

t.penup()
t.goto(-200, 0)
for i in range(n):
    t.color(colori[i%3])
    t.begin_fill()
    # disegna quadrato
    for _ in range(4):
        t.forward(lato)
        t.left(90)
    t.end_fill()
    # riposiziono la penna sul vertice in basso a sinistra del prossimo quadrato
    t.penup()
    t.forward(lato*3)
    t.right(90)
    lato *= 2
    t.forward(lato)
    t.left(180)
    t.pendown()

t.done()