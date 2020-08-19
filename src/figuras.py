import pygame
from abc import ABC, abstractmethod
from listener import *
from assets.herramientas import *
from assets.settings import *


class Figura(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Fondo(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoVentana"])
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Camino(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoCamino"])
        super().__init__(posicion)

    def dibujar(self, ventana):
        posicion = self.posicion.getPosicion()
        ventana.blit(self.imagen, posicion)
        ventana.blit(
            self.imagen, (posicion[0], settings["tamañoCamino"][1]))

    def mover(self, desplazamiento, ventana):
        x, y = self.posicion.getPosicion()
        alturaImagen = self.imagen.get_rect().height
        relativoY = y % alturaImagen
        ventana.blit(self.imagen, (x, relativoY - alturaImagen))
        if relativoY < settings['tamañoVentana'][1]:
            ventana.blit(self.imagen, (x, relativoY))
        self.posicion.actualizarY(y-desplazamiento)


class Personaje(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, (128, 128))
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        x, y = Listener.captarMouse()
        tamañoImagen = self.imagen.get_rect()
        distanciaVereda = (settings["tamañoVentana"]
                           [0] - settings["tamañoCamino"][0])/2
        condicionLimiteX = x >= distanciaVereda and x <= settings[
            "tamañoVentana"][0] - distanciaVereda
        condicionLimiteY = y >= settings["tamañoVentana"][1] * \
            0.1 and y <= settings["tamañoVentana"][1]*0.9
        if(condicionLimiteX and condicionLimiteY):
            self.posicion.actualizarX(Listener.captarMouse()[
                0]-tamañoImagen.width/2)
            self.posicion.actualizarY(Listener.captarMouse()[
                1]-tamañoImagen.height/2)
