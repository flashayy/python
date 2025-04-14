from sys import exit as sysexit
from random import randrange as rr
import pygame
pygame.init()

res = xres, yres =1920, 1080
screen = pygame.display.set_mode(res)

class Player():
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
    
    def draw(self, surface):
        pygame.draw.rect(screen, (rr(0, 256), rr(256), rr(256)), (self.x, self.y, self.a, self.b))
    
    def move_right(self):
        self.x += 1
        
    def move_left(self):
        self.x -= 1
        
    def move_down(self):
        self.y += 1
        
    def move_up(self):
        self.y -= 1
        
    def inc(self):
        self.a += 10
        self.b += 10
        
    def dec(self):
        self.a -= 10
        self.b -= 10
        
player_one = Player(150, 150, 200, 200)
        
hrame = True

while hrame:
    hodiny = pygame.time.Clock()
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            SystemExit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_q:
                player_one.inc()
            if udalost.key == pygame.K_e:
                player_one.dec()
                
    klavesy = pygame.key.get_pressed()

    if klavesy[pygame.K_a]:
        player_one.move_left()

    if klavesy[pygame.K_d]:
        player_one.move_right()

    if klavesy[pygame.K_w]:
        player_one.move_up()

    if klavesy[pygame.K_s]:
        player_one.move_down()
    
    screen.fill((0,0,0))
    player_one.draw(screen)
    pygame.display.update()
    hodiny.tick(50)
pygame.quit()
