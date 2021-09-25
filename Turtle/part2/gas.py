import numpy as np
import turtle as tt

number_of_turtles = 5

pool = [tt.Turtle(shape='circle') for _ in range(number_of_turtles)]
r = np.random.normal(loc=0, scale=50, size=(number_of_turtles, 2))
v = np.random.normal(loc=0, scale=10, size=(number_of_turtles, 2))
dt = 1

box_size = 200
hitbox_size = 20

tt.speed(0)
tt.penup()
tt.goto(-box_size, -box_size)
tt.pendown()
tt.forward(2 * box_size)
tt.left(90)
tt.forward(2 * box_size)
tt.left(90)
tt.forward(2 * box_size)
tt.left(90)
tt.forward(2 * box_size)

tt.ht()

for i, unit in enumerate(pool):
    unit.penup()
    unit.speed(0)
    unit.goto(*r[i])

while True:
    r += v * dt

    for i in range(number_of_turtles):
        for dim in (0, 1):
            if np.abs(r[i][dim]) >= box_size:
                r[i][dim] = box_size * np.sign(r[i][dim])
                v[i][dim] *= -1

        pool[i].goto(*r[i])

    for i in range(number_of_turtles):
        for j in range(i + 1, number_of_turtles):
            if np.linalg.norm(r[i] - r[j]) < hitbox_size:
                v1, x1 = v[i], r[i]
                v2, x2 = v[j], r[j]
                dx = x1 - x2
                dv = v1 - v2
                ldx = np.linalg.norm(dx) ** 2
                dvx = np.dot(dv, dx)
                v[i] = v1 - dx * dvx / ldx
                v[j] = v2 + dx * dvx / ldx
                r[i] = r[j] + hitbox_size * dx / np.linalg.norm(dx)