import turtle
import colorsys
import random
screen=turtle.Screen()
screen.title("Neon Infinity")
screen.setup(width=1.0, height=1.0)
turtle.hideturtle()
turtle.bgcolor("black")
turtle.pencolor("cyan")
turtle.speed(0)
turtle.penup()
turtle.goto(700,-320)
turtle.pendown()
l=1
b=1
turtle.pensize(2)
for i in range(254):
    turtle.forward(l)
    turtle.setheading(270)
    turtle.forward(b)
    turtle.setheading(180)
    l+=5.6
    turtle.forward(l)
    turtle.setheading(90)
    b+=2.801
    turtle.forward(b)
    turtle.setheading(0)
    h=random.random()
    color=colorsys.hsv_to_rgb(h,1,1)
    turtle.pencolor(color)
turtle.done()