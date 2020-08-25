#!/usr/bin/env python3
import pygame
from figuras import *
from posicion import *
from mensaje import *
from assets.settings import *
from boton import *

pygame.init()

ventana = pygame.display.set_mode(settings["tamañoVentana"])

# Mensajes iniciales GUI
mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion((0, 0)))
mensajeInstrucciones = Mensaje('img/fondoInstrucciones.png', Posicion((0, 0)))
#print(settings["coordenadaBotonJugar"])
#print(type(settings["coordenadaBotonJugar"]))
btnJugar = Boton('JUGAR', Posicion(settings["coordenadaBotonJugar"]))

btnAtras = Boton('ATRAS', Posicion(settings["coordenadaBotonAtras"]))
btnOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))
mensajeBienvenida.agregarBoton(btnJugar)
mensajeBienvenida.agregarBoton(btnAtras)
mensajeInstrucciones.agregarBoton(btnOk)

#mensajeBienvenida.mostrar(ventana)
#mensajeInstrucciones.mostrar(ventana)


mapa = Mapa()

mapa.agregarFigura(Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
mapa.agregarFigura(Camino('img/fondoCamino.png', Posicion(settings["coordenadaCamino"])))
mapa.agregarFigura(FiguraPregunta('img/pregunta.png', Posicion(settings["coordenadaFigPregunta"]), "s"))
mapa.agregarFigura(FiguraVida('img/vida4.png', Posicion(settings["coordenadaFigVida"])))
mapa.agregarFigura(Marcador('img/pregunta.png', Posicion(settings["coordenadaMarcador"]), 0))
mapa.agregarFigura(Personaje('img/personaje.png', Posicion(settings["coordenadaPersonaje"])))
mapa.agregarFigura(FiguraOpcion('img/botonA.png', Posicion(settings["coordenadaOpcion"][0])))
mapa.agregarFigura(FiguraOpcion('img/botonB.png', Posicion(settings["coordenadaOpcion"][1])))
mapa.agregarFigura(FiguraOpcion('img/botonC.png', Posicion(settings["coordenadaOpcion"][2])))


rutamayainiciado = True
estadomensajebienvenida = True

# def obtenerSegundos(ticksComienzo):
#    return ()

#game.time.get_ticks()-start_ticksmapa.dibujar()

while rutamayainiciado:
    # if obtenerSegundos(start_ticks) <= 5.0:
    #    camino.mover(10, ventana)
    mapa.mover(ventana)
    mapa.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rutamayainiciado = False
        pass
    pygame.display.update()
    