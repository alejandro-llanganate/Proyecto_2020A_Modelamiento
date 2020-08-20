import pygame
from assets.settings import *
from assets.herramientas import *
from posicion import *


class Boton:
    def __init__(self, tipo, posicion):
        self.tipo = tipo
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
        self._rect = pygame.Rect((0, 0), (100, 100))
        self.i = 0

    def render(self, ventana):
<<<<<<< HEAD
        ventana.blit(self.imagen, self.posicion.getPosicion())
        
    def onClic(self, event):
        rect = pygame.Rect(self.posicion.getPosicion(), (self.imagen.get_rect().width,self.imagen.get_rect().height) )
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if event.button == 1:  
                if rect.collidepoint(event.pos):
                    print('s') 
                    return (self.tipo, True)
        return (self.tipo, False) 

=======
        ventana.blit(self.imagen, self._rect)

    def event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self._rect.collidepoint(event.pos):  # is mouse over button
                    print("Hola mundo")
>>>>>>> 78278ddc68578d54b76e7c7c27cd61ccacdfcfac
