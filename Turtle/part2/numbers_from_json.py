import json
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

with open('font.json', 'r') as f:
	font = json.load(f)

number = input()

for i in number:
    draw(font[i], side=font['font size'])
    turtle.penup()
    turtle.forward(font['font size'] * 1.5)
    turtle.pendown()
