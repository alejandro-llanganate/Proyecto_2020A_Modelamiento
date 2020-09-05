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
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/obs1.jpg', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.getPosicion()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): 
            self.posicion.actualizarY(self.posicion.getPosicion()[1]-settings["tamañoVentana"][1]*0.03)
        else:
            self.posicion.actualizarY(settings["tamañoVentana"][1])
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])))

class ObstaculoB(Obstaculo):

    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/ob2.jpg', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.getPosicion()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): 
            self.posicion.actualizarY(self.posicion.getPosicion()[1]-settings["tamañoVentana"][1]*0.03)
        else:
            self.posicion.actualizarY(settings["tamañoVentana"][1])
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])))



class ObstaculoC(Obstaculo):

    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/obs3.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.getPosicion()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): 
            self.posicion.actualizarY(self.posicion.getPosicion()[1]-settings["tamañoVentana"][1]*0.03)
        else:
            self.posicion.actualizarY(settings["tamañoVentana"][1])
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])))