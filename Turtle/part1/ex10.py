import turtle
import math

turtle.speed(100000)

def draw_circ(a):
    a = a * 0.01
    n = 60
    phi = 360 / n
    for i in range(n):
        turtle.forward(a)
        turtle.left(phi)

N = 12

for i in range(N):
    draw_circ(1000)
    turtle.left(360/N)
