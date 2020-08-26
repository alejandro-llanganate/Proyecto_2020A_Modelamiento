import pygame
from time import time
from assets.herramientas import *
from figuras import *


pygame.init()


class AudioPregunta:
    def __init__(self, audio, letraRespuesta):
        self.audio = obtenerPathAbsoluto(audio, __file__)
        self.letraRespuesta = letraRespuesta

    def reproducir(self):
        pygame.mixer.music.load(self.audio)
        pygame.mixer.music.play(0)

    def notificarFinPregunta(self, opciones):
        for opcion in opciones:
            opcion.setVisibilidad(True)

    def getLetraRespuesta(self):
        return self.letraRespuesta