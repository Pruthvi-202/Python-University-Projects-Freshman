"""

File: project2py
Programmer: Pruthviraj Guduru
Date:9/13/2024
Description: This program is used to create an online drawing on the CSU Clock Tower

"""



# I imported the two modules I will need for this project.
import turtle
import math

#I created a screen and gave it a name.
wn = turtle.Screen()
wn.title("CSU Clock Tower")


#I created a Turtle, gave it a name, and gave it certain properties.
snake = turtle.Turtle()
snake.shape('arrow')
snake.pensize(2)
snake.fillcolor("royal blue")
snake.color("royal blue")

#This code is used to create the clock tower itself.
snake.left(90)
snake.forward(180)
snake.right(90)
snake.forward(15)
snake.left(90)
snake.forward(20)
snake.right(45)
snake.forward(50)
snake.right(90)
snake.forward(50)
snake.right(45)
snake.forward(20)
snake.left(90)
snake.forward(15)
snake.right(90)
snake.forward(180)
snake.right(90)
snake.forward(14)
snake.right(90)
snake.forward(33)
snake.left(90)
snake.forward((30 * math.sqrt(2)) + 30)
snake.left(90)
snake.forward(33)
snake.right(90)
snake.forward(14)

# I created a turtle named "crusher" and gave it various properties.
crusher = turtle.Turtle()
crusher.shape('turtle')
crusher.pensize(1)
crusher.fillcolor("red")
crusher.color("red")

# This code is used to create the bottom left pillar
crusher.backward(15)
crusher.left(90)
crusher.forward(35)
crusher.right(90)
crusher.forward(13.5)
crusher.right(90)
crusher.forward(35)

#This code is used to pick up the pen and make the bridge under the entrance arch.
crusher.penup()
crusher.goto(15,5)
crusher.pendown()
crusher.left(90)
crusher.forward(15)
crusher.left(90)
crusher.forward(20)
crusher.right(90)
crusher.forward(30 * math.sqrt(2))
crusher.right(90)
crusher.forward(20)
crusher.left(90)
crusher.forward(15)

#This code is used to create the bottom right pillar.
crusher.penup()
crusher.goto(100,0)
crusher.pendown()
crusher.forward(15)
crusher.left(90)
crusher.forward(35)
crusher.left(90)
crusher.forward(13.5)
crusher.left(90)
crusher.forward(35)

#This code is used to create the top left chimney.
crusher.penup()
crusher.goto(0,181)
crusher.pendown()
crusher.left(90)
crusher.forward(13.5)
crusher.left(90)
crusher.forward(30)
crusher.left(90)
crusher.forward(14.5)
crusher.left(90)
crusher.forward(30)

#This code is used to create the top right chimney.
crusher.penup()
crusher.goto(((50*math.sqrt(2))+15),(181))
crusher.pendown()
crusher.left(90)
crusher.forward(14.5)
crusher.left(90)
crusher.forward(30)
crusher.left(90)
crusher.forward(13.5)
crusher.left(90)
crusher.forward(30)

#This code creates the "bat" turtle and gives it properties.           
bat = turtle.Turtle()
bat.shape('circle')
bat.color('dark green')
bat.fillcolor('dark green')
bat.pensize(3)

#This code creates the clock.
bat.penup()
bat.goto((25*math.sqrt(2)+15),(140))
bat.pendown()
bat.circle(10)

wn = turtle.exitonclick()
#This project took me around 2 hours and 30 minutes to make.

