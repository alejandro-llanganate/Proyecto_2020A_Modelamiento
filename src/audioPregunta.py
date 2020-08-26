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
        self.audio = pygame.mixer.Sound(obtenerPathAbsoluto("p1.wav", __file__))
        print("Len: ", self.audio.get_length())

    def reproducir(self, opciones):
        #print("Pos: ", self.audio.get_pos())
        #print("Remaining: ", (self.audio.get_length() - self.audio.get_pos())*-1)
     
        self.audio.play()
  
        #print("Indicador: **", pygame.mixer.music.get_busy())
        #pygame.mixer.stop()
        #print("Stop: **", pygame.mixer.music.get_busy())

        for opcion in opciones:
            opcion.setVisibilidad()
        

    def getLetraRespuesta(self):
        return self.letraRespuesta
    
    
class ListaAudioPreguntas:
    def __init__(self):
        self.audios = []
    
    def agregarAudioPregunta(self, audio):
        self.audios.append(audio)