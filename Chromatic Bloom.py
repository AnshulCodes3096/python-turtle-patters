from turtle import *
from colorsys import *
title("Chromatic Bloom")
bgcolor("black")
pencolor("white")
speed(0)
hideturtle()
h=0
for i in range(72):
    pencolor(hsv_to_rgb(h,1,1))
    h+=0.02
    circle(180)
    circle(150)
    circle(120)
    circle(90)
    circle(60)
    circle(30)
    left(5)
done()
