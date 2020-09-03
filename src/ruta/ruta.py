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
        self.mapa = Mapa
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
        self.mostrarMensajesIniciales()
        
        # preconfiguraciones
        self.ventana = pygame.display.set_mode(settings["tamañoVentana"])
        pygame.display.set_caption(settings["nombre"])
        rutamayainiciado = True
        self.mapa = Mapa()

        audioPruebaSonido = AudioPregunta('sounds/p1.wav', "A")

        verificacion = Verificacion(audioPruebaSonido, self.mapa)

        solapamientoOpcionA = Solapamiento(30, verificacion)
        solapamientoOpcionB = Solapamiento(30, verificacion)
        solapamientoOpcionC = Solapamiento(30, verificacion)

        solapamientos = [solapamientoOpcionA,
                         solapamientoOpcionB, solapamientoOpcionC]

        self.mapa.agregarFigura(
            Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
        camino = Camino('img/fondoCamino.png',
                        Posicion(settings["coordenadaCamino"]))
        self.mapa.agregarFigura(camino)
        self.mapa.agregarFigura(FiguraVida(
            Posicion(settings["coordenadaFigVida"])))
        self.mapa.agregarFigura(Marcador('img/marcador.png',
                                    Posicion(settings["coordenadaMarcador"]), 0))
        self.mapa.agregarFigura(Personaje(
            'img/personaje.png', Posicion(settings["coordenadaPersonaje"]), solapamientos))

        opcionA = FiguraOpcion(
            'img/botonA.png', Posicion(settings["coordenadaOpcion"][0]), "A", solapamientoOpcionA)
        opcionB = FiguraOpcion(
            'img/botonB.png', Posicion(settings["coordenadaOpcion"][1]), "B", solapamientoOpcionB)
        opcionC = FiguraOpcion(
            'img/botonC.png', Posicion(settings["coordenadaOpcion"][2]), "C", solapamientoOpcionC)

        self.mapa.agregarFigura(opcionA)
        self.mapa.agregarFigura(opcionB)
        self.mapa.agregarFigura(opcionC)

        obstaculo = FabricaObstaculoA().crearObstaculo('img/obstaculo.png', Posicion(settings["coordenadaObstaculo"]))


        while rutamayainiciado:
            self.mapa.mover(self.ventana)
            self.mapa.dibujar(self.ventana)
            obstaculo.dibujar(self.ventana)
            audioPruebaSonido.reproducir(camino, self.mapa.obtenerOpciones())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rutamayainiciado = False
                    pygame.quit()
            pygame.display.update()

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
