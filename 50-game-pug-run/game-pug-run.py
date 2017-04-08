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
# vyctove typy
from enum import Enum

# objekty #####################################################################################

class Smer(Enum):
    VLEVO = 1
    VPRAVO = 2
    NAHORU = 3
    DOLU = 4

# objekt reprezentujici mopslika
class Mopslik:
    meObrazky = {
        Smer.VLEVO: "zatim zadny",
        Smer.VPRAVO: "zatim zadny",
        Smer.NAHORU: "zatim zadny",
        Smer.DOLU: "zatim zadny"
    }
    # konstruktor, ktery vytvori noveho mopslika
    def __init__(self):
        self.barva = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.bezim = Smer.VPRAVO
    # mopsliku, udelej krok vpravo
    def udelejKrokVpravo(self):
        self.x += 5
        self.bezim = Smer.VPRAVO
    def udelejKrokVlevo(self):
        self.x -= 10
        self.bezim = Smer.VLEVO
    def udelejKrokDolu(self):
        self.y += 10
        self.bezim = Smer.DOLU
    def udelejKrokNahoru(self):
        self.y -= 10
        self.bezim = Smer.NAHORU
    def nastavJakVypadam(self, kdyzJduVlevo, kdyzJduVpravo, kdyzJduNahoru, kdyzJduDolu):
        self.meObrazky[Smer.VLEVO] = kdyzJduVlevo
        self.meObrazky[Smer.VPRAVO] = kdyzJduVpravo
        self.meObrazky[Smer.NAHORU] = kdyzJduNahoru
        self.meObrazky[Smer.DOLU] = kdyzJduDolu
    def nakresliSe(self):
        # nakresli obrazek mopslika
        obrazovka.blit(self.meObrazky[self.bezim], (self.x, self.y))
        # nakresli mopslika grafikou
        #pygame.draw.rect(obrazovka, self.barva, (self.x, self.y, 50, 30))
        
# objekt reprezentujici dobrotu
class Dobrota:
    # konstruktor, ktery vytvori novou dobrotu
    def __init__(self):
        self.barva = (255, 0 , 0)
    def nastavJakVypadam(self, obrazekDobroty):
        self.obrazek = obrazekDobroty
    def nastavPozici(self, x, y):
        self.x = x
        self.y = y
    def nakresliSe(self):
        obrazovka.blit(self.obrazek, (self.x, self.y))

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

# dobrota
dobrota = Dobrota();

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
        
    # nakresli dobroty
    dobrota.nakresliSe()
    # nakresli mopslika jako posledniho, aby byl nahore nad ostatnimy sprity
    mopslik.nakresliSe()

# program #####################################################################################

# inicializace
pygame.init()
# nastaveni sirky a vysky aobrazovky
obrazovka = pygame.display.set_mode((sirkaObrazovky, vyskaObrazovky))
# nastaveni jmena okna
pygame.display.set_caption('Pug Run')

# natazeni obrazku
obrazekMopslikBeziVlevo = pygame.image.load("obrazky/mopslik-vlevo.png")
obrazekMopslikBeziVpravo = pygame.image.load("obrazky/mopslik-vpravo.png")
obrazekMopslikBeziNahoru = pygame.image.load("obrazky/mopslik-vlevo.png")
obrazekMopslikBeziDolu = pygame.image.load("obrazky/mopslik-vlevo.png")
obrazekDobrota = pygame.image.load("obrazky/kosticka.png")

# natazeni zvuku
zvukStek = pygame.mixer.Sound("zvuky/haf.ogg")
zvukStek.set_volume(50)
zvukStek.play()

# pouziti obrazku, zvuku, ...
mopslik.nastavJakVypadam(obrazekMopslikBeziVlevo, obrazekMopslikBeziVpravo, obrazekMopslikBeziNahoru, obrazekMopslikBeziDolu)
dobrota.nastavJakVypadam(obrazekDobrota)
dobrota.nastavPozici(random.randint(10,sirkaObrazovky), random.randint(10,vyskaObrazovky))

# nekonecna smycka hry
while True:    
    # zaciname znovu: vybarvi pozadi cernou barvou
    obrazovka.fill((255,255,255))
    # zpracuj udalosti klavesnice/mysi/... a nastav globalni promenne
    zpracujUdalosti(klavesnice)
    # pohni mopslike & spol
    pohniMopslikemAOstatnimyObjekty(klavesnice)    
    # v kazdem cyklu prekresli obrazovku do okna
    pygame.display.update()
    # ... a chvilku pockej
    time.sleep(0.03)




