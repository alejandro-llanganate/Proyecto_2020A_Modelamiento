from pygame import *
from posicion import *
from assets.settings import *
from assets.herramientas import *



class Boton:
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.posicion = posicion

    def render(self):
        pygame.blit(self.image)

    def onClic(self, function):
        function()
