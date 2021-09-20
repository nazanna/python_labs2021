import random
import turtle
import time

turtle.speed(0)
while True:
    a = random.random() * 10
    p = random.random() * 360

    turtle.forward(a)
    turtle.left(p)
