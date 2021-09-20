import turtle

def draw_star(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.left(180 - 180/n)

turtle.left(180)
draw_star(5, 200)

turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

draw_star(11, 200)
