import json
import turtle

def draw_from_coords(font_size, coords_list):
    x0, y0 = turtle.pos()

    def goto(r_rel):
        x_rel, y_rel = r_rel
        turtle.goto(x0 + x_rel * font_size, y0 + y_rel * font_size)

    turtle.penup()
    goto(coords_list[0])
    turtle.pendown()
    for coord in coords_list:
        goto(coord)

    turtle.penup()
    turtle.goto(x0, y0)
    turtle.pendown()

with open('font.json', 'r') as f:
	font = json.load(f)

font_size = font["font_size"]
spacing = font["spacing"]

turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()

for i in "0123456789ծ":
    draw_from_coords(font_size, font[i])
    turtle.penup()
    turtle.forward(spacing)
    turtle.pendown()