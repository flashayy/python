from random import randrange
import pygame
from sys import exit as sysexit

pygame.init()

display = pygame.display.set_mode((10,10))
velkost = 40
priestor = [" "] * velkost
hrac, okraj = "X", "#"
pozLO = velkost // 4
sirkaMax = velkost // 2
sirka = sirkaMax
pozH = velkost // 2
priestor[pozLO] = okraj
priestor[pozLO + sirka] = okraj
priestor[pozH] = hrac
skore = 0
RDUmax, RZSmin = 10, 8
RDU, RZS = RDUmax, RZSmin

def posunZnaku(pozicia, posun, znak, delta = 0):
    global priestor
    if 0 <= pozicia + posun < velkost and 0 <= pozicia + posun + delta < velkost:
        priestor[pozicia] = " "
        priestor[pozicia+posun] = znak
        return posun
    return 0

def berieMinus(pozicia, posun):
    if priestor[pozicia+posun] == "-" and RZS > RZSmin:        
        return -1
    return 0

def beriePlus(pozicia, posun):
    global priestor
    if priestor[pozicia+posun] == "+" and sirka < sirkaMax:
        priestor[pozLO+sirka] = " "
        priestor[pozLO+sirka+1] = okraj
        return 1
    return 0

def berieRDU(pozicia, posun):
    if priestor[pozicia+posun] == "0":
        return RDUmax
    return RDU

def umiestniPomoc(poleZnakov):
    global priestor
    for znak in poleZnakov:
        if randrange(10) == randrange(10):
            if znak not in priestor:
                pozPom = randrange(pozLO+1, pozLO+sirka)
                while  priestor[pozPom] != " ":
                    pozPom = randrange(pozLO+1, pozLO+sirka)
                priestor[pozPom] = znak

def zmensiSirku():
    global priestor
    priestor[pozLO+sirka] = " "
    priestor[pozLO+sirka-1] = okraj
    return -1

hrame = True

while hrame:
    hodiny = pygame.time.Clock()
    skore += 1
    RDU -= 1
    print("|" + "".join(priestor) + "| ")
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sysexit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_a:
                zmenaHraca = -1
            if udalost.key == pygame.K_d:
                zmenaHraca = 1
            RZS += berieMinus(pozH, zmenaHraca)
            sirka += beriePlus(pozH, zmenaHraca)
            RDU = berieRDU(pozH, zmenaHraca)
            pozH += posunZnaku(pozH, zmenaHraca, hrac)        
    zmenaCesty = randrange(-1,2)
    posunZnaku(pozLO, zmenaCesty, okraj, sirka)
    pozLO += posunZnaku(pozLO+sirka, zmenaCesty, okraj, -sirka)
    umiestniPomoc(["-","+","0"])
    if hrac not in priestor:
        print("havaria skore: " + str(skore) + " RZS: " + str(RZS) + " # -> #: " + str(sirka))
        hrame = False
    if RDU == 0:
        if randrange(10) == randrange(10):
            RZS += 1
        elif randrange(10) == randrange(10):
            sirka += zmensiSirku()
        else:
            RZS += 1
            sirka += zmensiSirku()
        RDU = RDUmax
    hodiny.tick(RZS)
pygame.quit()