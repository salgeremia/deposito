import turtle

s = turtle.getscreen()
t = turtle.Turtle()
l = int(input('Lunghezza quadrato: '))
for _ in range(4):
    t.forward(l)
    t.left(90)
t.shape('square')
for _ in range(4):
    t.forward(l*2)
    t.left(90)

turtle.done()
