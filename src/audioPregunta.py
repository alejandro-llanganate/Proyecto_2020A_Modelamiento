import pygame
from time import time
from assets.herramientas import *
from figuras import *


class AudioPregunta:
    def __init__(self, audio, letraRespuesta, opciones):
        self.audio = pygame.mixer.Sound(obtenerPathAbsoluto(audio, __file__))
        self.letraRespuesta = letraRespuesta
        self.opciones = opciones
        self.state = True

    def reproducir(self, camino):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_s] and camino.notificar() == False):
            self.state = False
        
        if(self.state and camino.notificar() == False):
            self.audio.play()

        if(self.state == False and camino.notificar() == False):
            pygame.mixer.stop()
            for opcion in self.opciones:
                opcion.setVisibilidad(True)

    def setState(value):
        self.state = value
    
    def getLetraRespuesta(self):
        return self.letraRespuesta