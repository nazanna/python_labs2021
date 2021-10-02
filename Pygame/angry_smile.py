import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((200, 200, 200))

yellow = (255, 255, 0)
black = (0, 0, 0)
red = (255, 0, 0)

draw.circle(screen, yellow, (200, 200), 100)
draw.circle(screen, black, (200, 200), 100, 2)

draw.rect(screen, black, (150, 250, 100, 20))

draw.circle(screen, red, (150, 180), 20)
draw.circle(screen, black, (150, 180), 20, 2)
draw.circle(screen, black, (150, 180), 10)

draw.circle(screen, red, (250, 180), 15)
draw.circle(screen, black, (250, 180), 15, 2)
draw.circle(screen, black, (250, 180), 8)

draw.polygon(screen, black, ((100, 127), (105, 117), (183, 168), (178, 175), (100, 127)))
draw.polygon(screen, black, ((220, 167), (300, 137), (304, 146), (224, 176), (220, 167)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()