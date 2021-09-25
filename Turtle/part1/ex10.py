import turtle

turtle.speed(0)

def draw_circ(a, n=60):
    a *= 0.01
    phi = 360 / n
    for i in range(n):
        turtle.forward(a)
        turtle.left(phi)

N = 12

for i in range(N):
    draw_circ(1000)
    turtle.left(360/N)
