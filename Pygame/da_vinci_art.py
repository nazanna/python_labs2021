import pygame
import pygame.draw as draw

from draw_objects import draw_ghost, draw_house, draw_ellipse

pygame.init()

COLORS = {'black': (0, 0, 0),
          'white': (255, 255, 255),
          'light_white_grey': (102, 102, 102),
#           'light_light_grey': (90, 90, 90, 127),
          'dark_light_grey': (77, 77, 77),
          'light_medium_grey': (51, 51, 51),
          'medium_medium_grey': (50, 50, 50, 127),
          'dark_medium_grey': (40, 40, 40, 127),
          'dark_grey': (26, 26, 26)}

FPS = 30
screen = pygame.display.set_mode((800, 1000))
surface = pygame.Surface((800, 1000), pygame.SRCALPHA)
screen.fill(COLORS['light_white_grey'])
#set screen

clock = pygame.time.Clock()
finished = False
#set time

while not finished:
    
    draw.rect(screen, COLORS['black'], (0, 471, 800, 529))
    
    draw.ellipse(screen, COLORS['white'], (640, 20, 190, 190))
    draw.ellipse(screen, COLORS['dark_light_grey'], (350, 50, 500, 80))
    draw.ellipse(screen, COLORS['light_medium_grey'], (40, 90, 600, 70))
    draw.ellipse(screen, COLORS['dark_light_grey'], (450, 150, 500, 80))
    draw.ellipse(screen, COLORS['dark_grey'], (400, 240, 600, 80))
    #draw background
    
    draw_house(screen, x0 = 560, y0 = 210, scale = 0.4, alpha = 127)
    draw_house(screen, x0 = 260, y0 = 340, scale = 0.4, alpha = 255)
    #draw houses
    
    draw_ellipse(screen, COLORS['medium_medium_grey'], (140, 420, 720, 80))
    draw_ellipse(screen, COLORS['dark_medium_grey'], (350, 510, 600, 50))
    draw_ellipse(screen, COLORS['light_light_grey'], (-100, 600, 500, 50))
    #draw clouds
    
    draw_house(screen, x0 = 0  , y0 = 450, scale = 0.4, alpha = 255)
    #draw houses
    
    draw_ghost(screen, x0 = 500, y0 = 700, scale = 1.0, alpha = 255)
    draw_ghost(screen, x0 = 450, y0 = 730, scale = 0.3, alpha = 100)
    draw_ghost(screen, x0 = 700, y0 = 500, scale = 0.3, alpha = 100)
    draw_ghost(screen, x0 = 750, y0 = 550, scale = 0.2, alpha = 100)
    draw_ghost(screen, x0 = 170, y0 = 800, scale = 0.6, alpha = 127, reversed = True)
    draw_ghost(screen, x0 = 200, y0 = 850, scale = 0.4, alpha = 127, reversed = True)
    #draw ghosts

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()