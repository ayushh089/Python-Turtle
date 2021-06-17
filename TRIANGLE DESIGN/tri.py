import turtle
j = 1
t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("Black")
t.pencolor("Yellow")
t.speed(0)
for i in range(300):
    t.forward(j)
    t.left(120)
    t.left(1)
    j += 1

turtle.done()
