#------------------------------------
# Created by Ayush Gupta
# Follow me on instagram @next_coders
# Please don't remove credits
#=-----------------------------------

import turtle
obj = turtle.Turtle()
obj.speed(10)
obj.pensize(3)


# outer circle
obj.begin_fill()
obj.fillcolor('#00a0de')
obj.right(210)
obj.circle(-120, 300)
obj.setheading(180)
obj.forward(120)
obj.setheading(0)
obj.end_fill()

# inner circle
obj.begin_fill()
obj.fillcolor("White")
obj.forward(10)
obj.right(210)
obj.circle(-100, 300)
obj.setheading(180)
obj.end_fill()


# red collar
obj.up()
obj.goto(0, 0)
obj.down()
obj.begin_fill()
obj.fillcolor('#e70010')
obj.forward(15)
obj.circle(5, 180)
obj.forward(150)
obj.circle(5, 180)
obj.forward(150)
obj.end_fill()


# left eye
obj.begin_fill()
obj.fillcolor("White")
obj.up()
obj.goto(25, 200)
obj.down()
rad = 30
obj.left(45)
for i in range(2):
    obj.circle(rad, 90)
    obj.circle(rad/2, 90)
obj.end_fill()

# righteye
obj.begin_fill()
obj.fillcolor("White")
obj.up()
obj.goto(60, 200)
obj.down()
rad = 30
obj.left(10)
for i in range(2):
    obj.circle(rad, 90)
    obj.circle(rad/2, 90)
obj.end_fill()

# eyebollLeftEye
obj.begin_fill()
obj.fillcolor("Black")
obj.up()
obj.goto(28, 180)
obj.down()
obj.circle(10)
obj.end_fill()

# right_eyw_ball
obj.begin_fill()
obj.fillcolor("Black")
obj.up()
obj.goto(65, 180)
obj.down()
obj.circle(10)
obj.end_fill()

# nose
obj.begin_fill()
obj.fillcolor("Red")
obj.up()
obj.goto(45, 155)
obj.down()
obj.circle(15)
obj.end_fill()


# mouthline
obj.up()
obj.goto(58, 130)
obj.down()
obj.setheading(270)
obj.fd(110)

# %mouth
obj.up()
obj.goto(15, 58)
obj.down()
obj.circle(40, 180)

# Lbeard1
obj.up()
obj.goto(29, 110)
obj.setheading(160)
obj.down()
obj.forward(60)
# Lbeard2
obj.up()
obj.goto(29, 90)
obj.setheading(180)
obj.down()
obj.forward(60)
# Lbeard3
obj.up()
obj.goto(29, 70)
obj.setheading(195)
obj.down()
obj.forward(60)

# Rbeard1
obj.up()
obj.goto(80, 110)
obj.setheading(20)
obj.down()
obj.forward(75)
# Rbeard2
obj.up()
obj.goto(80, 90)
obj.setheading(0)
obj.down()
obj.forward(80)
# Rbeard3
obj.up()
obj.goto(80, 70)
obj.setheading(350)
obj.down()
obj.forward(80)


# body
obj.begin_fill()
obj.fillcolor('#00a0de')
obj.up()
obj.goto(125, 0)
obj.left(45)
obj.down()
obj.forward(90)
obj.circle(-20, 250)
obj.seth(240)
obj.fd(80)
obj.seth(90)
obj.fd(15)
obj.backward(60)
obj.right(5)
obj.backward(70)
obj.seth(180)
obj.fd(50)


obj.seth(90)
obj.circle(30, 180)
obj.seth(180)
obj.fd(50)
obj.seth(95)
obj.fd(125)
obj.fd(-20)
obj.seth(210)
obj.fd(50)
obj.circle(-20, 250)
obj.seth(45)
obj.fd(58)

# collor corre
obj.up()
obj.goto(139, -10)
obj.down()
obj.pensize(2)
obj.circle(7, 180)
obj.end_fill()


# //lefthand
obj.up()
obj.goto(125, 0)
obj.seth(0)
obj.left(35)
obj.down()
obj.begin_fill()
obj.fillcolor("White")
obj.forward(90)
obj.circle(-20)
obj.end_fill()
obj.up()
obj.goto(125, 0)
obj.seth(0)
obj.left(35)


# left leg feet
obj.forward(90)
obj.circle(-20, 250)
obj.seth(240)
obj.fd(80)
obj.seth(90)
obj.fd(15)
obj.backward(60)
obj.right(5)
obj.backward(70)
obj.down()
obj.seth(0)
obj.circle(-10, 180)
obj.fd(50)
obj.begin_fill()
obj.fillcolor("White")
obj.circle(-10, 180)
obj.end_fill()


# right legfeet
obj.begin_fill()
obj.fillcolor("White")
obj.up()
obj.goto(0, -167)
obj.down()
obj.pensize(1)
obj.forward(40)
obj.pensize(3)
obj.circle(-10, 180)
obj.forward(40)
obj.circle(-10, 180)
obj.end_fill()


# for right hand 
obj.begin_fill()
obj.fillcolor("Blue")
obj.up()
obj.goto(125, 0)
obj.left(45)
obj.forward(90)
obj.circle(-20, 250)
obj.seth(240)
obj.fd(80)
obj.seth(90)
obj.fd(15)
obj.backward(60)
obj.right(5)
obj.backward(70)
obj.seth(180)
obj.fd(50)
obj.seth(90)
obj.circle(30, 180)
obj.seth(180)
obj.fd(50)
obj.seth(95)
obj.fd(125)
obj.fd(-32)
obj.seth(211)
obj.fd(49)
obj.down()
obj.begin_fill()
obj.pensize(2)
obj.fillcolor("White")
obj.circle(-19)
obj.end_fill()

# #stomach
obj.begin_fill()
obj.fillcolor("White")
obj.up()
obj.goto
obj.up()
obj.pensize(3)
obj.goto(16, -15)
obj.down()
obj.setheading(230)
obj.circle(60, 259)
obj.seth(180)
obj.forward(93.5)
obj.end_fill()


# pocket
obj.up()
obj.goto(35, -60)
obj.down()
obj.seth(270)
obj.circle(30, 180)
obj.seth(180)
obj.fd(60)

# collarbell
obj.up()
obj.goto(57, -5)
obj.down()
obj.begin_fill()
obj.fillcolor('#ffd200')
obj.circle(15, 450)
obj.end_fill()
obj.seth(0)
obj.pensize(2)
obj.left(4)
obj.fd(25)
obj.circle(3, 180)
obj.fd(25)
obj.seth(270)
obj.pensize(1)
obj.circle(20, 83)
obj.seth(90)
obj.pensize(3)
obj.fd(9)
obj.pensize(3)
obj.circle(2)

obj.hideturtle()

turtle.done()
