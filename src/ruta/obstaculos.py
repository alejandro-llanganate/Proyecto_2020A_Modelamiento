import pygame
from ruta.assets.herramientas import *
from ruta.assets.settings import *
from ruta.posicionMaya import *
from random import randint
from abc import ABC, abstractmethod


class Obstaculo(ABC):
    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class ObstaculoA(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/personaje.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]-30))
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass

class ObstaculoB(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/personaje2.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]-30))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass

class ObstaculoC(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/personaje3.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]-30))
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass