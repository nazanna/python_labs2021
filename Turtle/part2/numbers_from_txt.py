import turtle

# 1  2
# 3  4
# 5  6



def draw(number, side=40):
    turtle.penup()
    x0, y0 = turtle.pos()

    coords = [(x0, y0           ), (x0 + side, y0           ),
              (x0, y0 -     side), (x0 + side, y0 -     side),
              (x0, y0 - 2 * side), (x0 + side, y0 - 2 * side)]

    def goto(cell):
        turtle.goto(*coords[cell - 1])

    goto(number[0])
    turtle.pendown()

    for el in number:
        goto(el)

    turtle.penup()
    goto(1)
    turtle.pendown()

font = []

with open('font.txt', 'r') as f:
    lines = f.read().split('\n')
    for el in lines:
        print(el)
        font.append(tuple(map(int, el.split(' '))))

number = list(map(int,list(input())))

for i in number:
    draw(font[i])
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()
