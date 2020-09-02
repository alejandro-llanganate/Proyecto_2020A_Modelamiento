import pygame
from ruta.assets.herramientas import *
from ruta.assets.settings import *
from abc import ABC, abstractmethod


class Obstaculo(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class ObstaculoA(Obstaculo):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoPersonaje"])
        self.posicion = posicion
    
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())