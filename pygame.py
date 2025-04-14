import pygame
pygame.init()

res = xres, yres = 500, 500
screen = pygame.display.set_mode(res)

hrame = True
while hrame:
    hodiny = pygame.time.Clock()
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            SystemExit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_a:
                x -= 10
            if udalost.key == pygame.k_d:
                x += 10
    pygame.draw.rect(screen, (rr(0, 256), rr(256), rr(256)), (x, y, 200, 200))
    pygame.display.update()
    hodiny.tick(100)
pygame.quit()