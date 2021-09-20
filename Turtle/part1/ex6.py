import turtle

n = 12
turtle.shape('turtle')
turtle.speed(1)
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.right(360/n)
