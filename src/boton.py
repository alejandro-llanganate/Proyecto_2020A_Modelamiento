import pygame
from assets.settings import *
from assets.herramientas import *
from posicion import *


class Boton:
    def __init__(self, tipo, posicion):
        if tipo == "OK":
            self.imagen = pygame.image.load(
                obtenerPathAbsoluto('img/botonOk.png', __file__))
        elif tipo == "JUGAR":
            self.imagen = pygame.image.load(
                obtenerPathAbsoluto('img/botonJugar.png', __file__))
        elif tipo == "ATRAS":
            self.imagen = pygame.image.load(
                obtenerPathAbsoluto('img/botonAtras.png', __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoBoton"])
        self.posicion = posicion

    def render(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def onClic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self._rect.collidepoint(event.pos):
                    return true
