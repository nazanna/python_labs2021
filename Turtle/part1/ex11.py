import turtle

def draw_circ(a):
    a *= 0.01
    n = 60
    phi = 360 / n
    for i in range(n):
        turtle.forward(a)
        turtle.left(phi)


r = 300
dr = 100
while True:
    draw_circ(r)
    turtle.left(180)
    draw_circ(r)
    turtle.left(180)
    r += dr
