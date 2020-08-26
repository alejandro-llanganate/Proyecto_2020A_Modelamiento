import pygame
from time import time
from assets.herramientas import *
from figuras import *


pygame.init()


class AudioPregunta:
    def __init__(self, audio, letraRespuesta, figuraOpcion):
        self.audio = audio
        self.letraRespuesta = letraRespuesta
        self.figuraOpcion = figuraOpcion

    def cargarAudio(self):
        self.audio = pygame.mixer.Sound(
            obtenerPathAbsoluto("p1.wav", __file__))

    def reproducir(self, opciones, tiempo):
        #print("Pos: ", self.audio.get_pos())
        #print("Remaining: ", (self.audio.get_length() - self.audio.get_pos())*-1)
        # if(tiempo < self.audio.get_length()):
        # self.audio.play(-1)
        # else:
        # pygame.mixer.stop()
        # for opcion in opciones:
        # opcion.setVisibilidad(True)
        pygame.mixer.music.load(obtenerPathAbsoluto('p1.mp3', __file__))
        pygame.mixer.music.play(0)

    def dibujarOpciones(self, opciones):
        for opcion in opciones:
            opcion.setVisibilidad(True)

    def getLetraRespuesta(self):
        return self.letraRespuesta


class ListaAudioPreguntas:
    def __init__(self):
        self.audios = []

    def agregarAudioPregunta(self, audio):
        self.audios.append(audio)
