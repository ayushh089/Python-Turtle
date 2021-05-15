import turtle

t = turtle.Turtle()
t.pensize(2)
t.speed(3)
t.goto(0, -200)
t.seth(90)
t.goto(0, 300)
t.seth(0)
t.begin_fill()
t.fillcolor("#FF9933")
t.fd(180)
t.seth(270)
t.fd(50)
t.seth(180)
t.fd(180)
t.end_fill()

t.begin_fill()
t.fillcolor("#FFFFFF")
t.seth(270)  # down
t.fd(50)  # 50 units down
t.seth(0)  # set angle to 0
t.fd(180)
t.seth(90)
t.fd(50)
t.end_fill()


t.up()
t.goto(0, 200)
t.begin_fill()
t.fillcolor("#138808")
t.down()
t.seth(270)
t.fd(50)
t.seth(0)
t.fd(180)
t.seth(90)
t.fd(50)
t.end_fill()

t.up()
t.goto(90, 225)
t.down()
t.color("#000080")
t.pensize(2)
for i in range(24):
    t.color()
    t.fd(20)
    t.backward(20)
    t.left(18)

t.up()
t.goto(97, 245)

t.down()
t.pensize(3)
t.circle(22, 360)


t.up()
t.color("Black")
t.goto(50, 0)
t.write("Stay Safe,Stay Home", font=("Arial",
                                     15, "bold"))


t.hideturtle()
turtle.done()
