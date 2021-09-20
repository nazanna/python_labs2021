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

font = [(1, 2, 6, 5, 1),      # 0
        (3, 2, 6),            # 1
        (1, 2, 4, 5, 6),      # 2
        (1, 2, 3, 4, 5),      # 3
        (1, 3, 4, 2, 6),      # 4
        (2, 1, 3, 4, 6, 5),   # 5
        (2, 3, 5, 6, 4, 3),   # 6
        (1, 2, 3, 5),         # 7
        (1, 5, 6, 2, 1, 3, 4),# 8
        (4, 3, 1, 2, 4, 5)]   # 9

number = list(map(int,list(input())))

for i in number:
    draw(font[i])
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()
