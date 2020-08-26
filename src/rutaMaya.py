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
btnJugar = Boton('JUGAR', Posicion(settings["coordenadaBotonJugar"]))
btnAtras = Boton('ATRAS', Posicion(settings["coordenadaBotonAtras"]))
btnOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))
mensajeBienvenida.agregarBoton(btnJugar)
mensajeBienvenida.agregarBoton(btnAtras)
mensajeInstrucciones.agregarBoton(btnOk)

mensajeBienvenida.mostrar(ventana)
mensajeInstrucciones.mostrar(ventana)


mapa = Mapa()

camino = Camino('img/fondoCamino.png',Posicion(settings["coordenadaCamino"]))

mapa.agregarFigura(Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
mapa.agregarFigura(camino)
mapa.agregarFigura(FiguraVida('img/vida4.png', Posicion(settings["coordenadaFigVida"])))
mapa.agregarFigura(Marcador('img/pregunta.png', Posicion(settings["coordenadaMarcador"]), 0))
mapa.agregarFigura(Personaje('img/personaje.png', Posicion(settings["coordenadaPersonaje"])))

opcionA = FiguraOpcion('img/botonA.png', Posicion(settings["coordenadaOpcion"][0]))
opcionB = FiguraOpcion('img/botonB.png', Posicion(settings["coordenadaOpcion"][1]))
opcionC = FiguraOpcion('img/botonC.png', Posicion(settings["coordenadaOpcion"][2]))

mapa.agregarFigura(opcionA)
mapa.agregarFigura(opcionB)
mapa.agregarFigura(opcionC)


rutamayainiciado = True
estadomensajebienvenida = True


SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)

audio_prueba_sonido = AudioPregunta('sounds/p1.mp3', "B")

audio_prueba_sonido.reproducir()

while rutamayainiciado:
    mapa.mover(ventana)
    mapa.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == SONG_END:
            audio_prueba_sonido.notificarFinPregunta([opcionA, opcionB, opcionC])
        if event.type == pygame.QUIT:
            rutamayainiciado = False
        pass
    pygame.display.update()
