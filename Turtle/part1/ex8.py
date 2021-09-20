import turtle

turtle.shape('turtle')
turtle.speed(1000)
a = 5
i = 1

while True:
    turtle.forward(a * i)
    turtle.left(90)
    turtle.forward(a * i)
    turtle.left(90)
    i += 1
