import pygame
from ruta.boton import *
from ruta.posicionMaya import *
from ruta.assets.herramientas import *
import sys


class Mensaje:
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoVentana"])
        self.posicion = posicion
        self.boton = []
        self.visibilidad = False

    def agregarBoton(self, boton):
        self.boton.append(boton)

    def quitarBoton(self, boton):
        pass

    def mostrar(self, ventana):
        self.visibilidad = True
        
        while self.visibilidad:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                for btn in self.boton:
                    if (btn.obtenerTipo() == "OK" or btn.obtenerTipo() == "JUGAR" or btn.obtenerTipo() == "VOLVER_A_JUGAR") and btn.onClic(event)[1] == True:
                        self.visibilidad = False
            ventana.blit(self.imagen, self.posicion.getPosicion())
            for boton in self.boton:
                boton.render(ventana)
            pygame.display.update()
