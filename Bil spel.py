import pygame
import sys
import random
from pygame.locals import *

# Börian pygame
pygame.init()

ajastin = pygame.time.Clock()
FPS = 30

koko = (700,700)

ruutu=pygame.display.set_mode(koko)
pygame.display.set_caption("Auto peli")

Bil= pygame .image. load("Bil.png")
Buske = pygame .image. load("Buske.png")
Veg = pygame .image. load("Veg.png")
# storlek
pelx = 100
pely = 450
nopeus = 6
viholinennopeus =8

viholiset = [[20,350],[30,300],[80,50],[100,60],[130,120]]


# storlek
Bil = pygame.transform.scale(Bil,(250,250))
Bil = pygame.transform.rotate(Bil,90)

Veg = pygame.transform.scale(Veg,(700,700))
Buske = pygame.transform.scale(Buske,(300,300))

def peruna():

    #Händelser 
    tapahtumat =pygame.event.get()  
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT:
            pygame.quit()

            sys.exit()
 # spel logik 
          
def porkkana():
    # bakgrund
    ruutu.blit(Veg,(0,0))
    global pelx
    global pely
   # spelre
    nappaimet = pygame.key.get_pressed()
    if nappaimet[pygame.K_RIGHT ]:
        pelx += nopeus

    if nappaimet[pygame.K_LEFT]:
        pelx -= nopeus

    if pelx < -120:
        pelx = -120
    if pelx > 450:
        pelx = 450
# fiende 
    for viholinen in viholiset:
        ruutu.blit(Buske,viholinen)
        viholinen[1]+=viholinennopeus
        if viholinen[1] > 690:
           viholinen[1] = -300
           viholinen[0]  = random.randint(0,700)

# annat
  
    ruutu.blit(Bil,(pelx,pely))
    pygame.display.flip()

#Spel lop

while True:
    peruna()
    porkkana()
    ajastin.tick(FPS)


   

