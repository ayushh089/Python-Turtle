import turtle
obj = turtle.Turtle()
obj.speed(10)

# heart
obj.begin_fill()
obj.fillcolor("red")
obj.left(50)
obj.forward(200)

obj.circle(85, 180)
obj.up()
obj.goto(0, 0)
obj.down()
obj.right(100)
obj.forward(200)
obj.circle(-82.5, 180)
obj.end_fill()


#I
obj.up()
obj.goto(-300, 0)
obj.setheading(180)
obj.down()
obj.backward( 80)
obj.up()
obj.goto(-260, 0)
obj.right(90)
obj.down()
obj.forward(300)
obj.setheading(0)
obj.forward(40)
obj.forward(-80)

#U
obj.up()
obj.goto(300,300)
obj.down()
obj.setheading(270)
obj.forward(260)
obj.circle(50,180)
obj.forward(260)

obj.hideturtle()
turtle.done()
