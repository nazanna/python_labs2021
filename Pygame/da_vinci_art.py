import pygame
import pygame.draw as draw

from draw_objects import draw_ghost, draw_house

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

    draw_house(surface, screen, x0=0, y0=97, scale=0.9)
    draw_ghost(surface, screen, x0=500, y0=700, scale=1)

    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()