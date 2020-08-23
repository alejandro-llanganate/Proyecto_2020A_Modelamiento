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
    settings["tamañoVentana"][0]*0.45, settings["tamañoVentana"][1]*0.85))

mensajeBienvenida.agregarBoton(btnJugar)
mensajeBienvenida.agregarBoton(btnAtras)
mensajeInstrucciones.agregarBoton(btnOk)

rutamayainiciado = True
estadomensajebienvenida = True
mensajeBienvenida.mostrar(ventana)
mensajeInstrucciones.mostrar(ventana)


def obtenerSegundos(ticksComienzo):
    return (pygame.time.get_ticks()-start_ticks) / 1000


start_ticks = pygame.time.get_ticks()

while rutamayainiciado:
    fondoJuego.dibujar(ventana)
    camino.dibujar(ventana)
    if obtenerSegundos(start_ticks) <= 5.0:
        camino.mover(10, ventana)
    personaje.dibujar(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rutamayainiciado = False
        pass
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
    myfont = pygame.font.SysFont("arial", 60)
    # render text
    label = myfont.render("Some text!", 1, (255, 255, 255))
    ventana.blit(label, (settings["tamañoVentana"][0]/2.5,
                         settings["tamañoVentana"][1]/2.5))  # personaje.mover()
    pygame.display.update()
