from ruta.figuras import *
from ruta.audioPregunta import *
from ruta.assets.herramientas import *
from time import sleep


class Verificacion:

    _numeroPreguntasContestadas = 0

    def __init__(self, audioPregunta, mapa, puntaje):
        self.mapa = mapa
        self.respuestaPregunta = audioPregunta.obtenerLetraRespuesta()
        self.puntaje = puntaje

    def verificarSeleccion(self, letraSeleccionada):
        self._numeroPreguntasContestadas += 1
        print(f"Numero de preguntas contestadas: {self._numeroPreguntasContestadas}")   
        opciones = self.mapa.obtenerOpciones()

        if(self.respuestaPregunta == letraSeleccionada):
            pygame.mixer.music.load(obtenerPathAbsoluto('sounds/sonidoRespuestaCorrecta.mp3', __file__))
            pygame.mixer.music.play(0)
            sleep(3)
            self.mapa.actualizar(True) # True para actualizar la visibilidad de las opcines
            self.puntaje.incrementar()
        else:
            pygame.mixer.music.load(obtenerPathAbsoluto('sounds/sonidoRespuestaIncorrecta.mp3', __file__))
            pygame.mixer.music.play(0)
            sleep(3)
            self.mapa.actualizar(False) # False para actualizar la FiguraVida y restar una vida

    def comunicarSolapamientoObstaculo(self, valor): # comunica a mapa el mensaje de la verificación en Solapamiento de que se solapó un obstáculo 
        if valor:
            self.mapa.actualizar(False) # False para actualizar la FiguraVida, la visibilidad de opciones y para restar una vida
     
    def reiniciarNumeroPreguntasContestadas(self):
        self._numeroPreguntasContestadas = 0

    def obtenerNumeroPreguntasContestadas(self):
        return self._numeroPreguntasContestadas    