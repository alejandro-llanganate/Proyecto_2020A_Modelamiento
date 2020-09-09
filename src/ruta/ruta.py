#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

from juego import *
import pygame
import os
import sys
from ruta.assets.settings import *
from ruta.audioPregunta import *
from ruta.solapamiento import *
from ruta.posicionMaya import *
from ruta.fabricas import *
from ruta.figuras import *
from ruta.mensaje import *
from ruta.puntaje import *
from ruta.boton import *

sys.path.append('../juego.py')



class Ruta(Juego):
    def __init__(self):
        self.mapa = Mapa()
        self.puntaje = Puntaje       
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])

    def mostrarMensajesIniciales(self):
        pygame.display.set_caption(settings["nombre"])

        # creación de botones
        botonJugar = Boton('JUGAR', Posicion(settings["coordenadaBotonJugar"]))
        botonAtras = Boton('VOLVER_AL_MUSEO', Posicion(settings["coordenadaBotonAtras"]))
        botonOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))

        # creación de mensajes con sus botones respectivos
        mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion((0, 0)))
        mensajeBienvenida.agregarBoton(botonJugar)
        mensajeBienvenida.agregarBoton(botonAtras)

        mensajeInstrucciones = Mensaje('img/fondoInstrucciones.png', Posicion((0, 0)))
        mensajeInstrucciones.agregarBoton(botonOk)

        # Visualización de mensajes
        mensajeBienvenida.mostrar(self.ventana)
        mensajeInstrucciones.mostrar(self.ventana)


    def iniciarJuego(self):
        
        pygame.init() # carga los modulos de la librería pygame

        pygame.mouse.set_cursor(*pygame.cursors.tri_left) # cambia la apariencia del cursor por el diseño "tri_left"

        self.mostrarMensajesIniciales()

        rutamayainiciado = True 

        btnVolverAtras = Boton('VOLVER_AL_MUSEO', Posicion(settings["coordenadaBotonAtras"]))
        btnVolverJugar = Boton('VOLVER_A_JUGAR', Posicion(settings["coordenadaBotonJugar"]))

        mensajeGameOver = Mensaje('img/fondoAvisoPerdiste.png', Posicion((0,0)))
        mensajeGameOver.agregarBoton(btnVolverAtras)
        mensajeGameOver.agregarBoton(btnVolverJugar)
        
        mensajeGanaste = Mensaje('img/fondoAvisoGanaste.png', Posicion((0,0)))
        mensajeGanaste.agregarBoton(btnVolverAtras)
        mensajeGanaste.agregarBoton(btnVolverJugar)

        puntaje = Puntaje(4, 1000)
        
        pregunta1 = AudioPregunta('sounds/pregunta1.wav', "C")
        pregunta2 = AudioPregunta('sounds/pregunta2.wav', "B")
        pregunta3 = AudioPregunta('sounds/pregunta3.wav', "C")
        pregunta4 = AudioPregunta('sounds/pregunta4.wav', "B")

        preguntas = Playlist()

        preguntas.añadirAudioPregunta(pregunta1)
        preguntas.añadirAudioPregunta(pregunta2)
        preguntas.añadirAudioPregunta(pregunta3)
        preguntas.añadirAudioPregunta(pregunta4)

        verificacion = Verificacion(pregunta1, self.mapa, puntaje)

        solapamientoOpcionA = SolapamientoConOpcion(30, verificacion)
        solapamientoOpcionB = SolapamientoConOpcion(30, verificacion)
        solapamientoOpcionC = SolapamientoConOpcion(30, verificacion)

        solapamientosConOpcion = [solapamientoOpcionA, solapamientoOpcionB, solapamientoOpcionC]

        self.mapa.agregarFigura(Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
        camino = Camino('img/fondoCamino.png', Posicion(settings["coordenadaCamino"]), preguntas)
        
        solapamientoConObstaculo = SolapamientoConObstaculo(30, verificacion, camino)
        
        self.mapa.agregarFigura(camino)
        self.mapa.agregarFigura(FiguraVida(Posicion(settings["coordenadaFigVida"])))
        self.mapa.agregarFigura(Marcador('img/marcador.png', Posicion(settings["coordenadaMarcador"]), puntaje))

        opcionA = FiguraOpcion('img/botonA.png', Posicion(settings["coordenadaOpcion"][0]), "A", solapamientoOpcionA)
        opcionB = FiguraOpcion('img/botonB.png', Posicion(settings["coordenadaOpcion"][1]), "B", solapamientoOpcionB)
        opcionC = FiguraOpcion('img/botonC.png', Posicion(settings["coordenadaOpcion"][2]), "C", solapamientoOpcionC)

        self.mapa.agregarFigura(opcionA)
        self.mapa.agregarFigura(opcionB)
        self.mapa.agregarFigura(opcionC)

        self.mapa.agregarFigura(Personaje('img/personaje.png', Posicion(settings["coordenadaPersonaje"]), solapamientosConOpcion, solapamientoConObstaculo))

        while rutamayainiciado:
            self.verificarCondiciones(mensajeGameOver, mensajeGanaste, verificacion)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rutamayainiciado = False
                    pygame.quit()
            pygame.display.update()

    def verificarCondiciones(self, mensajeGameOver, mensajeGanaste, verificacion):
        if self.mapa.obtenerVidasActuales() >= 1:
            self.mapa.mover(self.ventana)
            if verificacion.obtenerNumeroPreguntasContestadas() == 4:
                pygame.mouse.set_visible(True)
                self.reiniciarJuego(self.mapa.obtenerFiguraVida(), self.mapa.obtenerCamino(), verificacion)
                mensajeGanaste.mostrar(self.ventana)
        else: 
            pygame.mouse.set_visible(True)
            self.reiniciarJuego(self.mapa.obtenerFiguraVida(), self.mapa.obtenerCamino(), verificacion)
            mensajeGameOver.mostrar(self.ventana)
        
        self.mapa.dibujar(self.ventana)

    def reiniciarJuego(self, figuraVida, camino, verificacion):
        figuraVida.reiniciarNumeroDeVidas()
        camino.reiniciarIteradores()
        verificacion.reiniciarNumeroPreguntasContestadas()

    def salirJuego(self):
        pass