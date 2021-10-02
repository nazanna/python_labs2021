import pygame
import pygame.draw as draw

from draw_objects import draw_ghost, draw_house, draw_ellipse_alpha

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1000))
surface = pygame.Surface((800, 1000), pygame.SRCALPHA)

screen.fill((102, 102, 102))

clock = pygame.time.Clock()
finished = False

while not finished:
    
    draw.rect(screen, (0, 0, 0), (0, 471, 800, 529))

    draw.ellipse(screen, (255, 255, 255), (640, 20, 190, 190))
    draw.ellipse(screen, (77, 77, 77), (350, 50, 500, 80))
    draw.ellipse(screen, (51, 51, 51), (40, 90, 600, 70))
    draw.ellipse(screen, (77, 77, 77), (450, 150, 500, 80))
    draw.ellipse(screen, (26, 26, 26), (400, 240, 600, 80))

    draw_house(screen, x0=560, y0=210, scale=0.4, alpha=127)
    draw_house(screen, x0=260, y0=340, scale=0.4, alpha=255)

    draw_ellipse_alpha(screen, (50, 50, 50, 127), (140, 420, 720, 80))
    draw_ellipse_alpha(screen, (40, 40, 40, 127), (350, 510, 600, 50))
    draw_ellipse_alpha(screen, (90, 90, 90, 127),(-100, 600, 500, 50))

    draw_house(screen, x0=0  , y0=450, scale=0.4, alpha=255)

    draw_ghost(screen, x0=500, y0=700, scale=1.0, alpha=255)
    draw_ghost(screen, x0=450, y0=730, scale=0.3, alpha=100)
    draw_ghost(screen, x0=700, y0=500, scale=0.3, alpha=100)
    draw_ghost(screen, x0=750, y0=550, scale=0.2, alpha=100)
    draw_ghost(screen, x0=170, y0=800, scale=0.6, alpha=127, reversed=True)
    draw_ghost(screen, x0=200, y0=850, scale=0.4, alpha=127, reversed=True)


    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()