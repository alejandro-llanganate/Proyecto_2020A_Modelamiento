import pygame
from boton import *
from posicion import *
from assets.herramientas import *


class Mensaje:
    visible = True

    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoVentana"])
        self.boton = []
        self.posicion = posicion

    def agregarBoton(self, boton):
        self.boton.append(boton)

    def quitarBoton(self, boton):
        pass

    def mostrar(self, ventana):
        while True:
            ventana.blit(self.imagen, self.posicion.getPosicion())
            for boton in self.boton:
                boton.render(ventana)
               # boton.onclic(evento)
            for event in pygame.event.get():
                pass
                # event_handler
            pygame.display.update()

    def mover(self):
        pass
