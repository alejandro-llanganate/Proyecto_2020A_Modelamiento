#!/usr/bin/env python3
import pygame
from figuras import *
from posicion import *
from mensaje import *
from assets.settings import *


pygame.init()

ventana = pygame.display.set_mode(settings["tamañoVentana"])
fondoJuego = Fondo('img/fondoJuego.png', Posicion(0, 0))
camino = Camino('img/fondoCamino.png', Posicion(291, 0))
personaje = Personaje('img/personaje.png', Posicion(129*4, 100))
mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion(0, 0))

while True:
    while True:
        mensajeBienvenida.mostrar(ventana)
        pygame.display.update()

    fondoJuego.dibujar(ventana)
    camino.dibujar(ventana)
    camino.mover(10, ventana)
    personaje.dibujar(ventana)
    for event in pygame.event.get():
        pass
    personaje.mover()
    pygame.display.update()
