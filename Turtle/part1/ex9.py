import turtle
import math

def draw_poly(n, r):

    b = math.pi * (1 - 2 / n) / 2

    a = 2 * r * math.sin(math.pi / n)
    phi = 360 / n

    turtle.penup()
    turtle.goto(-r * math.cos(b), -r * math.sin(b))

    turtle.pendown()


    for i in range(n):
        turtle.forward(a)
        turtle.left(phi)

for i in range(1, 11):
    draw_poly(i + 2, i * 20)
