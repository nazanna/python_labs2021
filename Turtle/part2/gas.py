import random
import turtle

number_of_turtles = 20


pool = [turtle.Turtle(shape='circle') for _ in range(number_of_turtles)]
vx   = [random.random() * 100 - 50 for _ in range(number_of_turtles)]
vy   = [random.random() * 100 - 50 for _ in range(number_of_turtles)]
x    = [random.randint(-200, 200)  for _ in range(number_of_turtles)]
y    = [random.randint(-200, 200)  for _ in range(number_of_turtles)]

turtle.penup()
turtle.speed(0)
turtle.goto(-200, -200)
turtle.pendown()
turtle.goto(-200, 200)
turtle.goto(200, 200)
turtle.goto(200, -200)
turtle.goto(-200, -200)
turtle.ht()

for i, unit in enumerate(pool):
    unit.penup()
    unit.speed(0)
    unit.goto(x[i], y[i])

dt = 0.1
while True:
    for i in range(number_of_turtles):
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt

        if x[i] >= 200 or x[i] <= -200:
            x[i] = 400 * (x[i] >= 200) - 200
            vx[i] *= -1

        if y[i] >= 200 or y[i] <= -200:
            y[i] = 400 * (y[i] >= 200) - 200
            vy[i] *= -1

        pool[i].goto(x[i], y[i])

    for i in range(number_of_turtles):
        for j in range(i, number_of_turtles):
            if (x[i] - x[j])*(x[i] - x[j]) + \
               (y[i] - y[j])*(y[i] - y[j]) <= 100:
                vx[i] *= -1
                vy[i] *= -1

                vx[j] *= -1
                vy[j] *= -1
