import pygame
from sys import exit as sysexit
pygame.init()
class Auticko():
    def __init__(ja, obrazok, x,y, pohyb, rozmery):
        ja.pozicia = [x,y]
        ja.pohyb = pohyb
        ja.sprite = pygame.image.load(obrazok)
        ja.rozmery = rozmery
    def dolava(ja):
        if ja.pozicia[0] > 0 :
            ja.pozicia[0] -= ja.pohyb
    def doprava(ja):
        if ja.pozicia[0] < ja.rozmery[0] - 100:
            ja.pozicia[0] += ja.pohyb
    def hore(ja):
        if ja.pozicia[1] > 0:
            ja.pozicia[1] -= ja.pohyb
    def dole(ja):
        if ja.pozicia[1] < ja.rozmery[1] - 100:
            ja.pozicia[1] += ja.pohyb

rozmery = (800, 600)
okno = pygame.display.set_mode(rozmery)
FPS = 60
Hra = True
auto = Auticko("auto.png", 200, 200, 5, rozmery)
while Hra:
    hodiny = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sysexit()
    klavesy = pygame.key.get_pressed()
    if klavesy[pygame.K_LEFT]:
        auto.dolava()
    if klavesy[pygame.K_RIGHT]:
        auto.doprava()
    if klavesy[pygame.K_DOWN]:
        auto.dole()
    if klavesy[pygame.K_UP]:
        auto.hore()
    okno.fill((0,0,0))
    okno.blit(auto.sprite,auto.pozicia)
    pygame.display.update()
    hodiny.tick(FPS)
pygame.quit()

