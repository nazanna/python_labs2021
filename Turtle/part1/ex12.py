import turtle

def draw_half_circ(a, n=60):
    a = a * 0.01
    phi = 360 / n
    for i in range(n//2):
        turtle.forward(a)
        turtle.left(phi)


turtle.penup()
turtle.backward(200)
turtle.pendown()

turtle.right(90)

while True:
    draw_half_circ(500)
    draw_half_circ(200)
