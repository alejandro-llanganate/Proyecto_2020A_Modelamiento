#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                       Clase Mensaje
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.assets.herramientas import *
from ruta.posicionMaya import *
from ruta.boton import *


class Mensaje:
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoVentana"])
        self.posicion = posicion
        self.visibilidad = False
        self.listaBotones = []

    def agregarBoton(self, boton):
        self.listaBotones.append(boton)

    def quitarBoton(self, boton):
        self.listaBotones.remove(boton)

    def mostrar(self, ventana):
        self.visibilidad = True
        
        while self.visibilidad:
            ventana.blit(self.imagen, self.posicion.getPosicion()) # Se dibuja el fondo del mensaje respectivo

            for boton in self.listaBotones: # para dibujar cada uno de los botones en el mensaje
                boton.render(ventana)
            
            for event in pygame.event.get(): 
                for boton in self.listaBotones:
                    # Los botones "OK", "JUGAR" y "VOLVER_A_JUGAR" si son seleccionados unicamente cerrarán el mensaje respectivo 
                    if (boton.obtenerTipo() == "OK" or boton.obtenerTipo() == "JUGAR" or boton.obtenerTipo() == "VOLVER_A_JUGAR") and boton.onClic(event)[1]:
                        self.visibilidad = False
            
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
