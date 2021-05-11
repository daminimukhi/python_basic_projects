import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(2) #method is used to change the speed of the turtle by the value of the argument that it takes. Return or set the turtle’s speed.

for i in range(6):
    for colours in {"red", "magenta", "blue", "cyan", "green", "yellow", "orange", "white" }:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()