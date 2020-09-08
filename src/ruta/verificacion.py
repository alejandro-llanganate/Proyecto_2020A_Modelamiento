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
            self.mapa.actualizar(True)
            self.puntaje.incrementar()
        else:
            pygame.mixer.music.load(obtenerPathAbsoluto('sounds/sonidoRespuestaIncorrecta.mp3', __file__))
            pygame.mixer.music.play(0)
            sleep(3)
            self.mapa.actualizar(False)

    def notificarSolapamiento(self, valor):
        if valor:
            self.mapa.actualizar(False)
    
    def reiniciarNumeroPreguntasContestadas(self):
        self._numeroPreguntasContestadas = 0

    def obtenerNumeroPreguntasContestadas(self):
        return self._numeroPreguntasContestadas    