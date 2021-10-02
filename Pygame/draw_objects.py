import pygame
import pygame.draw as draw

ghost_body_coords = [(58, 48),
                   (53, 73),
                   (42, 94),
                   (37, 106),
                   (26, 125),
                   (20, 133),
                   (14, 149),
                   (2, 169),
                   (1, 174),
                   (19, 172),
                   (34, 168),
                   (52, 177),
                   (65, 184),
                   (81, 205),
                   (92, 207),
                   (97, 206),
                   (107, 202),
                   (118, 190),
                   (132, 179),
                   (144, 177),
                   (157, 180),
                   (179, 180),
                   (186, 166),
                   (192, 148),
                   (199, 139),
                   (210, 137),
                   (223, 132),
                   (226, 127),
                   (226, 108),
                   (221, 94),
                   (212, 87),
                   (194, 74),
                   (139, 37),
                   (120, 21),]


def rect_scale(surface, color, coords, x0, y0, scale, width=0):
    x, y, w, h = coords
    x = x0 + x * scale
    y = y0 + y * scale
    w *= scale
    h *= scale

    draw.rect(surface, color, (x, y, w, h), width)


def polygon_scale(surface, color, coords, x0, y0, scale, width=0, reversed=False):
    coords_new = []
    if reversed:
        for coord in coords:
            x, y = coord
            x = x0 - x * scale
            y = y0 + y * scale
            coords_new.append((x, y))
    else:
        for coord in coords:
            x, y = coord
            x = x0 + x * scale
            y = y0 + y * scale
            coords_new.append((x, y))
    draw.polygon(surface, color, coords_new, width=0)


def circle_scale(surface, color, center, radius, x0, y0, scale, width=0, reversed=False):
    x, y = center
    x = x0 + (x * scale) * (1 - 2 * reversed)
    y = y0 + y * scale
    draw.circle(surface, color, (x, y), radius * scale, width=0)


def draw_house(surface, x0=0, y0=0, scale=1, alpha=255):

    brown_building = (43, 34, 0, alpha)
    brown_window = (43, 17, 0, alpha)
    yellow_window = (212, 170, 0, alpha)
    skin_window = (72, 62, 55, alpha)
    black_roof = (0, 0, 0, alpha)
    grey_fence = (26, 26, 26, alpha)


    rect_scale(surface, brown_building, (40, 150, 410, 570), x0, y0, scale)
    
    rect_scale(surface, brown_window, (85, 550, 80, 100), x0, y0, scale)
    rect_scale(surface, brown_window, (205 , 550, 80, 100), x0, y0, scale)
    rect_scale(surface, yellow_window, (325, 550, 80, 100), x0, y0, scale)
    
    for i in range(4):
        rect_scale(surface, skin_window, (70 + 105 * i, 150, 40, 210), x0, y0, scale)
    
    polygon_scale(surface, black_roof, [(0, 150), (60, 100), (430, 100), (490, 150)], x0, y0, scale)
    rect_scale(surface, grey_fence, (0, 370, 490, 60), x0, y0, scale)
    
    rect_scale(surface, grey_fence, (10, 320, 10, 50), x0, y0, scale)
    rect_scale(surface, grey_fence, (470, 320, 10, 50), x0, y0, scale)
    rect_scale(surface, grey_fence, (20, 300, 450, 20), x0, y0, scale)

    
    for i in range(5):
        rect_scale(surface, grey_fence, (60 + i * 87, 320, 20, 50), x0, y0, scale)
    
    rect_scale(surface, grey_fence, (100, 50, 10, 75), x0, y0, scale)
    rect_scale(surface, grey_fence, (120, 0 , 30, 130), x0, y0, scale)
    rect_scale(surface, grey_fence, (290, 70, 10, 30), x0, y0, scale)
    rect_scale(surface, grey_fence, (390, 45, 15, 85), x0, y0, scale)



def draw_ghost(surface, x0=0, y0=0, scale=1, alpha=255, reversed=False):
    grey_ghost = (179, 179, 179, alpha)
    eye_blue_ghost = (135, 205, 222, alpha)
    eye_black_ghost = (0, 0, 0, alpha)
    eye_whie_ghost = (255, 255, 255, alpha)

    circle_scale(surface, grey_ghost, (90, 35), 35, x0, y0, scale, reversed=reversed)

    
    
    polygon_scale(surface, grey_ghost, ghost_body_coords, x0, y0, scale, reversed=reversed)
   
    circle_scale(surface, eye_blue_ghost, (71, 34), 10, x0, y0, scale, reversed=reversed)
    circle_scale(surface, eye_whie_ghost, (71, 34), 5, x0, y0, scale, reversed=reversed)
    circle_scale(surface, eye_black_ghost, (68, 35), 4, x0, y0, scale, reversed=reversed)


    circle_scale(surface, eye_blue_ghost, (103, 26), 10, x0, y0, scale, reversed=reversed)
    circle_scale(surface, eye_whie_ghost, (103, 26), 5, x0, y0, scale, reversed=reversed)
    circle_scale(surface, eye_black_ghost, (100, 27), 4, x0, y0, scale, reversed=reversed)

