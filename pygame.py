from sys import exit as sysexit
from random import randrange as rr
import pygame
pygame.init()

res = xres, yres = 500, 500
screen = pygame.display.set_mode(res)

x, y = 150, 150
a, b = 200, 200

hrame = True
while hrame:
    hodiny = pygame.time.Clock()
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            SystemExit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_q:
                a += 10
                b += 10
            if udalost.key == pygame.K_e:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, a, b))
                a -= 10
                b -= 10
                
        klavesy = pygame.key.get_pressed()    
        if klavesy [pygame.K_a]:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, a, b))
                x -= 1
        if klavesy [pygame.K_d]:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, a, b))
                x += 1
    pygame.draw.rect(screen, (rr(0, 256), rr(256), rr(256)), (x, y, a, b))
    pygame.display.update()
    hodiny.tick(100)
pygame.quit()
