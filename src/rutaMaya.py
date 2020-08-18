#!/usr/bin/env python3
import pygame
from figuras import *
from posicion import *
from mensaje import *
from assets.settings import *
from boton import *

pygame.init()

ventana = pygame.display.set_mode(settings["tamañoVentana"])
fondoJuego = Fondo('img/fondoJuego.png', Posicion(0, 0))
camino = Camino('img/fondoCamino.png', Posicion(291, 0))
personaje = Personaje('img/personaje.png', Posicion(129*4, 100))
mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion(0, 0))
mensajeInstrucciones = Mensaje('img/fondoInstrucciones.png', Posicion(0, 0))

btnJugar = Boton('JUGAR', Posicion(
    settings["tamañoVentana"][0]*0.7, settings["tamañoVentana"][1]*0.75))

btnAtras = Boton('ATRAS', Posicion(
    settings["tamañoVentana"][0]*0.17, settings["tamañoVentana"][1]*0.75))

btnOk = Boton('OK', Posicion(
    settings["tamañoVentana"][0]*0.45, settings["tamañoVentana"][1]*0.75))

mensajeBienvenida.agregarBoton(btnJugar)
mensajeBienvenida.agregarBoton(btnAtras)
mensajeInstrucciones.agregarBoton(btnOk)

while True:
    mensajeInstrucciones.mostrar(ventana)
    mensajeBienvenida.mostrar(ventana)
    fondoJuego.dibujar(ventana)
    camino.dibujar(ventana)
    camino.mover(10, ventana)
    personaje.dibujar(ventana)
    for event in pygame.event.get():
        pass
    personaje.mover()
    pygame.display.update()
