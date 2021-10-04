import pygame
import pygame.draw as draw
from ghost_body import ghost_body_coords

def draw_rect(surface, color, rect, width = 0):
    """
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    rect - объект pygame.Rect
    width = 0 - толщина обводки
    """
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    draw.rect(shape_surf, color, shape_surf.get_rect(), width)
    surface.blit(shape_surf, rect)

def draw_circle(surface, color, center, radius, width = 0):
    '''
    surface -  объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    center - координаты центра
    radius - радиус
    width = 0 - толщина обводки
    '''
    
    target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    draw.circle(shape_surf, color, (radius, radius), radius, width)
    surface.blit(shape_surf, target_rect)

def draw_polygon(surface, color, points, width = 0):
    '''
    surface -  объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    points - координаты точек
    width = 0 - толщина обводки
    '''   
    
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    draw.polygon(shape_surf, color, [(x - min_x, y - min_y) for x, y in points], width)
    surface.blit(shape_surf, target_rect)

def draw_ellipse(surface, color, rect, width = 0):
    '''
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    rect - объект pygame.Rect
    width = 0 - толщина обводки
    '''    
    
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, shape_surf.get_rect(), width)
    surface.blit(shape_surf, rect)

def rect_scale(surface, color, coords, x0, y0, scale, width = 0):
    '''
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    coords - левый верхний угол, ширина, высота
    x0, y0 - перемещение левого верхнего угла
    scale - изменение размера сторон
    width = 0 - толщина обводки
    '''   
    
    x, y, w, h = coords
    x = x0 + x * scale
    y = y0 + y * scale
    w *= scale
    h *= scale
    #setting coordinates
    
    draw_rect(surface, color, (x, y, w, h), width)
    #direct rendering


def polygon_scale(surface, color, coords, x0, y0, scale, width = 0, reversed = False):
    '''
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    coords - координаты точек
    x0, y0 - перемещение фигуры
    scale - изменение размера сторон
    width = 0 - толщина обводки
    reversed = False - отражение относительно вертикали
    '''
    
    coords_new = []
    for coord in coords:
        x, y = coord
        x = x0 + x * scale * ((1 - 2 * reversed))
        y = y0 + y * scale
        coords_new.append((x, y))
    #setting coordinates
    
    draw_polygon(surface, color, coords_new, width) 
    #direct rendering


def circle_scale(surface, color, center, radius, x0, y0, scale, width = 0, reversed = False):
    '''
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    center - координаты центра
    radius - радиус
    scale - изменение размера сторон
    width = 0 - толщина обводки 
    reversed = False - отражение относительно вертикали
    '''
    
    x, y = center
    x = x0 + (x * scale) * (1 - 2 * reversed)
    y = y0 + y * scale
    #setting coordinates
    
    draw_circle(surface, color, (x, y), radius * scale, width)
    #direct rendering


def draw_house(surface, x0 = 0, y0 = 0, scale = 1, alpha = 255):
    '''
    surface - объект pygame.Surface
    x0, y0 - перемещение фигуры
    scale - изменение размера сторон
    alpha = 255 - насыщенность цветов
    '''
    
    COLORS_HOUSE = {'brown_building': (43, 34, 0, alpha), 
                    'brown_window': (43, 17, 0, alpha), 
                    'yellow_window': (212, 170, 0, alpha), 
                    'skin_window': (72, 62, 55, alpha), 
                    'black_roof': (0, 0, 0, alpha), 
                    'grey_fence': (26, 26, 26, 255)}

    rect_scale(surface, COLORS_HOUSE['brown_building'], (40, 150, 410, 570), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['brown_window'], (85, 550, 80, 100), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['brown_window'], (205 , 550, 80, 100), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['yellow_window'], (325, 550, 80, 100), x0, y0, scale)
    
    for i in range(4):
        rect_scale(surface, COLORS_HOUSE['skin_window'], (70 + 105 * i, 150, 40, 210), x0, y0, scale)
    #draw windows
    
    polygon_scale(surface, COLORS_HOUSE['black_roof'], [(0, 150), (60, 100), (430, 100), (490, 150)], x0, y0, scale)
    #draw roof
    
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (0, 370, 490, 60), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (10, 320, 10, 50), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (470, 320, 10, 50), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (20, 300, 450, 20), x0, y0, scale)

    for i in range(5):
        rect_scale(surface, COLORS_HOUSE['grey_fence'], (60 + i * 87, 320, 20, 50), x0, y0, scale)
    
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (100, 50, 10, 75), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (120, 0 , 30, 130), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (290, 70, 10, 30), x0, y0, scale)
    rect_scale(surface, COLORS_HOUSE['grey_fence'], (390, 45, 15, 85), x0, y0, scale)
    #draw fence


def draw_ghost(surface, x0 = 0, y0 = 0, scale = 1, alpha = 255, reversed = False):
    '''
    surface - объект pygame.Surface
    x0, y0 - перемещение фигуры
    scale - изменение размера сторон
    alpha = 255 - насыщенность цветов
    reversed = False - отражение относительно вертикали
    '''
    COLOR_GHOST = {'grey_ghost': (179, 179, 179, alpha),
    'eye_blue_ghost': (135, 205, 222, alpha),
    'eye_black_ghost': (0, 0, 0, alpha),
    'eye_whie_ghost': (255, 255, 255, alpha),
    'grey_contour': (200, 200, 200)}

    polygon_scale(surface, COLOR_GHOST['grey_ghost'], ghost_body_coords, x0, y0, scale, reversed = reversed)
    polygon_scale(surface, COLOR_GHOST['grey_contour'], ghost_body_coords, x0, y0, scale, reversed = reversed, width = 1)
    #draw body
    
    circle_scale(surface, COLOR_GHOST['eye_blue_ghost'], (71, 34), 10, x0, y0, scale, reversed = reversed)
    circle_scale(surface, COLOR_GHOST['eye_whie_ghost'], (71, 34), 5, x0, y0, scale, reversed = reversed)
    circle_scale(surface, COLOR_GHOST['eye_black_ghost'], (68, 35), 4, x0, y0, scale, reversed = reversed)
    circle_scale(surface, COLOR_GHOST['eye_blue_ghost'], (103, 26), 10, x0, y0, scale, reversed = reversed)
    circle_scale(surface, COLOR_GHOST['eye_whie_ghost'], (103, 26), 5, x0, y0, scale, reversed = reversed)
    circle_scale(surface, COLOR_GHOST['eye_black_ghost'], (100, 27), 4, x0, y0, scale, reversed = reversed)
    #draw eyes