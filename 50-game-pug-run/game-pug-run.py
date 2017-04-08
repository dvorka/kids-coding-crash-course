#!/usr/bin/env python

# knihovny ####################################################################################

# knihovna pro vytvareni her
import pygame
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
# knihovna zakladnich funkci
import sys
# knihovna nahodnych cisel
import random
# knihovna casu
import time

# objekty #####################################################################################

# objekt reprezentujici mopslika
class Mopslik:
    # konstruktor, ktery vytvori noveho mopslika
    def __init__(self):
        self.barva = (255, 255, 255)
        self.x = 0
        self.y = 0
    # mopsliku, udelej krok vpravo
    def udelejKrokVpravo(self):
        self.x += 5
    def udelejKrokVlevo(self):
        self.x -= 10
    def udelejKrokDolu(self):
        self.y += 10
    def udelejKrokNahoru(self):
        self.y -= 10
    def nastavObrazek(self, obrazek):
        self.toJsemJa = obrazek
    def nakresliSe(self):
        # nakresli mopslika
        #pygame.draw.rect(obrazovka, self.barva, (self.x, self.y, 50, 30))
        obrazovka.blit(self.toJsemJa, (self.x, self.y))
        
# objekt reprezentujici dobrotu
class Dobrota:
    # konstruktor, ktery vytvori novou dobrotu
    def __init__(self):
        self.barva = (255, 0 , 0)

# objekt reprezentujici zlodeje mopsliku
class Zlodej:
    # konstruktor, ktery vytvori noveho zlodeje
    def __init__(self):
        self.barva = (255, 0 , 0)
        
# objekt reprezentujici klavesnici
class Klavesnice:
    def __init__(self):
        self.vlevoStisknuta = False
        self.vpravoStisknuta = False
        self.nahoruStisknuta = False
        self.doluStisknuta = False

# globalni promenne ###########################################################################

# obrazovka
sirkaObrazovky = 1000
vyskaObrazovky = 600

# mopslik
mopslik = Mopslik()

# klavesnice
klavesnice = Klavesnice()

# funkce ######################################################################################

# funkce ukoncujici hru
def ukonciHru():
    pygame.quit()
    sys.exit()

# funkce ktera zpracuje vsechny udalosti klavesnice, ktere 
# se staly od minuleho prekresleni a nastavi odpovidajici 
# globalni promenne
def zpracujUdalosti(klavesnice):
    for udalost in GAME_EVENTS.get():
        # pokud byla stisknuta klavesa
        if udalost.type == pygame.KEYDOWN:
            # pokud byla stisknuta klavesa VLEVO
            if udalost.key == pygame.K_LEFT:
                klavesnice.vlevoStisknuta = True
            # pokud byla stisknuta klavesa VPRAVO
            if udalost.key == pygame.K_RIGHT:
                klavesnice.vpravoStisknuta = True
            # pokud byla stisknuta klavesa NAHORU
            if udalost.key == pygame.K_UP:
                klavesnice.nahoruStisknuta = True
            # pokud byla stisknuta klavesa DOLU
            if udalost.key == pygame.K_DOWN:
                klavesnice.doluStisknuta = True
            # pokud byla stisknuta klavesa ESCAPE
            if udalost.key == pygame.K_ESCAPE:
                ukonciHru()
                
        # pokud byla puvodne stisknuta klavesa zvednuta
        if udalost.type == pygame.KEYUP:
            # pokud byla stisknuta klavesa VLEVO
            if udalost.key == pygame.K_LEFT:
                klavesnice.vlevoStisknuta = False
            # pokud byla stisknuta klavesa VPRAVO
            if udalost.key == pygame.K_RIGHT:
                klavesnice.vpravoStisknuta = False
            # pokud byla stisknuta klavesa NAHORU
            if udalost.key == pygame.K_UP:
                klavesnice.nahoruStisknuta = False
            # pokud byla stisknuta klavesa DOLU
            if udalost.key == pygame.K_DOWN:
                klavesnice.doluStisknuta = False
                
        # pokud prisla udalost pro ukonceni hry
        if udalost.type == GAME_GLOBALS.QUIT:
            ukonciHru()

# pohni objekty - obrazky mopslika, dobrot, chytace - podle promenny a casu
def pohniMopslikemAOstatnimyObjekty(klavesnice):
    if klavesnice.vpravoStisknuta:
        mopslik.udelejKrokVpravo()
    if klavesnice.vlevoStisknuta:
        mopslik.udelejKrokVlevo()
    if klavesnice.doluStisknuta:
        mopslik.udelejKrokDolu()
    if klavesnice.nahoruStisknuta:
        mopslik.udelejKrokNahoru()
        
    mopslik.nakresliSe()

# program #####################################################################################

# inicializace
pygame.init()
# nastaveni sirky a vysky aobrazovky
obrazovka = pygame.display.set_mode((sirkaObrazovky, vyskaObrazovky))
# nastaveni jmena okna
pygame.display.set_caption('Pug Run')

# natazeni obrazku
obrazek = pygame.image.load("obrazky/mopslik.png")
mopslik.nastavObrazek(obrazek)
# natazeni zvuku
zvukStek = pygame.mixer.Sound("zvuky/bell.ogg")
zvukStek.set_volume(50)
zvukStek.play()

# nekonecna smycka hry
while True:    
    # zaciname znovu: vybarvi pozadi cernou barvou
    obrazovka.fill((0,0,0))
    # zpracuj udalosti klavesnice/mysi/... a nastav globalni promenne
    zpracujUdalosti(klavesnice)
    # pohni mopslike & spol
    pohniMopslikemAOstatnimyObjekty(klavesnice)    
    # v kazdem cyklu prekresli obrazovku do okna
    pygame.display.update()
    # ... a chvilku pockej
    time.sleep(0.03)




