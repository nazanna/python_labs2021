import turtle

turtle.shape('turtle')

for i in range(10):
    turtle.pendown()
    turtle.forward(10 * (1 + 2 * i))
    turtle.left(90)
    turtle.forward(10 * (1 + 2 * i))
    turtle.left(90)
    turtle.forward(10 * (1 + 2 * i))
    turtle.left(90)
    turtle.forward(10 * (1 + 2 * i))
    turtle.penup()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
