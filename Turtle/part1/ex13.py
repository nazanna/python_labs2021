import turtle
import math

def draw_circ(r):
    n = 60
    phi = 360 / n
    a = 2 * r * math.sin(math.pi / n)

    for i in range(n):
        turtle.forward(a)
        turtle.left(phi)

def draw_half_circ(r):
    n = 60
    phi = 360 / n
    a = 2 * r * math.sin(math.pi / n)

    for i in range(n//2):
        turtle.forward(a)
        turtle.left(phi)

turtle.speed(10)

turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.begin_fill()
draw_circ(200)
turtle.color("#ffff00")
turtle.end_fill()

turtle.penup()
turtle.goto(100, 70)
turtle.pendown()
turtle.color("#000000")
turtle.begin_fill()
draw_circ(20)
turtle.color("#00ff00")
turtle.end_fill()

turtle.penup()
turtle.goto(-90, 70)
turtle.pendown()
turtle.color("#000000")
turtle.begin_fill()
draw_circ(20)
turtle.color("#00ff00")
turtle.end_fill()

turtle.penup()
turtle.goto(-90, -30)
turtle.pendown()
turtle.right(90)
turtle.color("#ff0000")
turtle.width(30)
draw_half_circ(100)
