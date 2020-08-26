#!/usr/bin/env python3
import pygame
from figuras import *
from posicion import *
from mensaje import *
from assets.settings import *
from boton import *
from audioPregunta import *
from time import time


pygame.init()

ventana = pygame.display.set_mode(settings["tamañoVentana"])

# Mensajes iniciales GUI
mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion((0, 0)))
mensajeInstrucciones = Mensaje('img/fondoInstrucciones.png', Posicion((0, 0)))
# print(settings["coordenadaBotonJugar"])
# print(type(settings["coordenadaBotonJugar"]))
btnJugar = Boton('JUGAR', Posicion(settings["coordenadaBotonJugar"]))

btnAtras = Boton('ATRAS', Posicion(settings["coordenadaBotonAtras"]))
btnOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))
mensajeBienvenida.agregarBoton(btnJugar)
mensajeBienvenida.agregarBoton(btnAtras)
mensajeInstrucciones.agregarBoton(btnOk)

# mensajeBienvenida.mostrar(ventana)
# mensajeInstrucciones.mostrar(ventana)


mapa = Mapa()

mapa.agregarFigura(
    Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
mapa.agregarFigura(Camino('img/fondoCamino.png',
                          Posicion(settings["coordenadaCamino"])))
mapa.agregarFigura(FiguraVida(
    'img/vida4.png', Posicion(settings["coordenadaFigVida"])))
mapa.agregarFigura(Marcador('img/pregunta.png',
                            Posicion(settings["coordenadaMarcador"]), 0))
mapa.agregarFigura(Personaje('img/personaje.png',
                             Posicion(settings["coordenadaPersonaje"])))

opcionA = FiguraOpcion(
    'img/botonA.png', Posicion(settings["coordenadaOpcion"][0]))
opcionB = FiguraOpcion(
    'img/botonB.png', Posicion(settings["coordenadaOpcion"][1]))
opcionC = FiguraOpcion(
    'img/botonC.png', Posicion(settings["coordenadaOpcion"][2]))
mapa.agregarFigura(opcionA)
mapa.agregarFigura(opcionB)
mapa.agregarFigura(opcionC)


rutamayainiciado = True
estadomensajebienvenida = True

# def obtenerSegundos(ticksComienzo):
#    return ()

# game.time.get_ticks()-start_ticksmapa.dibujar()

t1 = time()

audio_prueba_sonido = AudioPregunta(None, None, None)
audio_prueba_sonido.cargarAudio()
tiempo = time() - t1
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
audio_prueba_sonido.reproducir([opcionA, opcionB, opcionC], tiempo)
while rutamayainiciado:
    # if obtenerSegundos(start_ticks) <= 5.0:
    #    camino.mover(10, ventana)

    mapa.mover(ventana)
    mapa.dibujar(ventana)

    #tiempo = time() - t1
    #audio_prueba_sonido.reproducir([opcionA, opcionB, opcionC], tiempo)

    #print("Tiempo: ",tiempo)

    for event in pygame.event.get():
        if event.type == SONG_END:
            audio_prueba_sonido.dibujarOpciones([opcionA, opcionB, opcionC])
        if event.type == pygame.QUIT:
            rutamayainiciado = False
        pass
    pygame.display.update()
