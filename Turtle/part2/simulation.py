import turtle
import time
x = -800
y = 0
vx = 30
vy = 80
dt = 0.1
g = -10
ey = 0.9
ex = cd0.9
k = -0.02
turtle.speed(1000)
turtle.goto(1000, 0)
turtle.goto(-1000, 0)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.speed(100)
while True:
    x += vx * dt
    y += vy * dt + g * dt**2 /2
    vy += g * dt + k * vy * dt
    vx += k * vx * dt
    if y <= 0:
        y = 0
        vy *= -ey
        vx *= ex
    turtle.goto(x, y)
