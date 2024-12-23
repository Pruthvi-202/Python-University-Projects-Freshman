import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape('turtle')
alex.speed(10)
#turtle.begin_fill()

turtle.pensize(5)
turtle.pencolor('blue')
turtle.fillcolor('lightblue')

alex.forward(150)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(50)

#turtle.end_fill()
alex.goto(50,40)
alex.setheading(45)
x,y = alex.pos()
print(x,y)
