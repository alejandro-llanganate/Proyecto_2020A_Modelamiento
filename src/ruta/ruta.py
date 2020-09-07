from juego import *
import pygame
import os
import sys
from ruta.assets.settings import *
from ruta.figuras import *
from ruta.solapamiento import *
from ruta.posicionMaya import *
from ruta.mensaje import *
from ruta.boton import *
from ruta.audioPregunta import *
from ruta.puntaje import *
from ruta.fabricas import *


sys.path.append('../juego.py')


class Ruta(Juego):
    def __init__(self):
        self.mapa = Mapa()
        self.puntaje = Puntaje       

    def mostrarMensajesIniciales(self):
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])
        mensajeBienvenida = Mensaje(
            'img/fondoBienvenida.png', Posicion((0, 0)))
        mensajeInstrucciones = Mensaje(
            'img/fondoInstrucciones.png', Posicion((0, 0)))
        btnJugar = Boton('JUGAR', Posicion(
            settings["coordenadaBotonJugar"]))
        btnAtras = Boton('ATRAS', Posicion(
            settings["coordenadaBotonAtras"]))
        btnOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))
        mensajeBienvenida.agregarBoton(btnJugar)
        mensajeBienvenida.agregarBoton(btnAtras)
        mensajeInstrucciones.agregarBoton(btnOk)
        mensajeBienvenida.mostrar(self.ventana)
        mensajeInstrucciones.mostrar(self.ventana)


    def iniciarJuego(self):
        
        pygame.init()
        
        self.mostrarMensajesIniciales()
        
        # preconfiguraciones
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])
        pygame.display.set_caption(settings["nombre"])
        rutamayainiciado = True

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

        solapamientosConOpcion = [solapamientoOpcionA,
                         solapamientoOpcionB, solapamientoOpcionC]

        self.mapa.agregarFigura(
            Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
        camino = Camino('img/fondoCamino.png',
                        Posicion(settings["coordenadaCamino"]), preguntas)
        solapamientoConObstaculo = SolapamientoConObstaculo(30, verificacion, camino)
        self.mapa.agregarFigura(camino)
        self.mapa.agregarFigura(FiguraVida(
            Posicion(settings["coordenadaFigVida"])))
        self.mapa.agregarFigura(Marcador('img/marcador.png',
                                    Posicion(settings["coordenadaMarcador"]), puntaje))
        self.mapa.agregarFigura(Personaje(
            'img/personaje.png', Posicion(settings["coordenadaPersonaje"]), solapamientosConOpcion, solapamientoConObstaculo))

        opcionA = FiguraOpcion(
            'img/botonA.png', Posicion(settings["coordenadaOpcion"][0]), "A", solapamientoOpcionA)
        opcionB = FiguraOpcion(
            'img/botonB.png', Posicion(settings["coordenadaOpcion"][1]), "B", solapamientoOpcionB)
        opcionC = FiguraOpcion(
            'img/botonC.png', Posicion(settings["coordenadaOpcion"][2]), "C", solapamientoOpcionC)

        self.mapa.agregarFigura(opcionA)
        self.mapa.agregarFigura(opcionB)
        self.mapa.agregarFigura(opcionC)

        while rutamayainiciado:
            
            if self.verificarCondiciones(self.mapa.obtenerVidasActuales()):
                self.mapa.mover(self.ventana)
            else:
                pygame.mouse.set_visible(True)
                self.mostrarMensajesIniciales()
            self.mapa.dibujar(self.ventana)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rutamayainiciado = False
                    pygame.quit()
            pygame.display.update()

    def reiniciarJuego(self, figuraVida, camino):
        figuraVida.setVidas(0)
        camino.setIteradorObstaculo(0)
        camino.setIteradorPlaylist(0) 

    def salirJuego(self):
        pass

    def verificarCondiciones(self, numeroDeVidas):
        return numeroDeVidas >= 1