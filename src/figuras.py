import pygame
from abc import ABC, abstractmethod
from listener import *
from assets.herramientas import *
from assets.settings import *


class Figura(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Fondo(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoVentana"])
        super().__init__(posicion)
        

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Camino(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoCamino"])
        self.posicion = posicion
        #super().__init__(posicion)

    def dibujar(self, ventana):
        posicion = self.posicion.getPosicion()
        #ventana.blit(self.imagen, posicion)
        ventana.blit(self.imagen, (posicion[0], settings["tamañoCamino"][1]))

    def mover(self, desplazamiento, ventana):
        estado_movimiento = True
        x, y = self.posicion.getPosicion()
        alturaImagen = self.imagen.get_rect().height
        relativoY = y % alturaImagen
        self.distancia = abs(y)
        if(  self.distancia <= alturaImagen*2):
            ventana.blit(self.imagen, (x, relativoY - alturaImagen))
            if relativoY < settings['tamañoVentana'][1]:
                ventana.blit(self.imagen, (x, relativoY))
            self.posicion.actualizarY(y-desplazamiento)
        else:

            ventana.blit(self.imagen, settings["coordenadaCamino"])
        #return estado_movimiento
        # (ti*2,ti*4,ti*3,6000,)

    def notificar(self, estado_movimiento):
        pass



class Personaje(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, (128, 128))
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        x, y = Listener.captarMouse()
        tamañoImagen = self.imagen.get_rect()
        distanciaVereda = (settings["tamañoVentana"]
                           [0] - settings["tamañoCamino"][0])/2
        condicionLimiteX = x >= distanciaVereda and x <= settings[
            "tamañoVentana"][0] - distanciaVereda
        condicionLimiteY = y >= settings["tamañoVentana"][1] * \
            0.1 and y <= settings["tamañoVentana"][1]*0.9
        if(condicionLimiteX and condicionLimiteY):
            self.posicion.actualizarX(Listener.captarMouse()[
                0]-tamañoImagen.width/2)
            self.posicion.actualizarY(Listener.captarMouse()[
                1]-tamañoImagen.height/2)


class FiguraPregunta(Figura):
    def __init__(self, imagen, posicion, contenido):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoFigPregunta"])
        self.posicion = posicion
        self.contenido = contenido

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class FiguraVida(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoFigVida"])
        self.posicion = posicion

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class FiguraOpcion(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoOpcion"])
        self.posicion = posicion

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Marcador(Figura):
    def __init__(self, imagen, posicion, puntaje):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoMarcador"])
        self.posicion = posicion
        self.puntaje = puntaje


    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass


class Mapa(Figura):
    def __init__(self):
        self.dictFiguras = dict()
        self.dictFiguras['fondo'] = None
        self.dictFiguras['camino'] = None
        self.dictFiguras['marcador'] = None
        self.dictFiguras['figuraVida'] = None
        self.dictFiguras['figuraOpcion'] = list()
        self.dictFiguras['personaje'] = None
        self.dictFiguras['figuraPregunta'] = None


    def agregarFigura(self, figura):
        if isinstance(figura, Camino):
            self.dictFiguras['camino'] = figura
        elif isinstance(figura, Marcador):
            self.dictFiguras['marcador'] = figura
        elif isinstance(figura, Fondo):
            self.dictFiguras['fondo'] = figura
        elif isinstance(figura, Personaje):
            self.dictFiguras['personaje'] = figura
        elif isinstance(figura, FiguraVida):
            self.dictFiguras['figuraVida'] = figura
        elif isinstance(figura, FiguraPregunta):
            self.dictFiguras['figuraPregunta'] = figura
        elif isinstance(figura, FiguraOpcion):
            self.dictFiguras['figuraOpcion'].append(figura)
    
    def accederLista(self):
        return self.dictFiguras
        
    def dibujar(self, ventana):
        for key in self.dictFiguras:
            if key != 'figuraOpcion' and key != 'personaje':
                self.dictFiguras[key].dibujar(ventana)
        for opcion in self.dictFiguras['figuraOpcion']:
            opcion.dibujar(ventana)
        self.dictFiguras['personaje'].dibujar(ventana)
            
    def mover(self, ventana):
        self.dictFiguras['camino'].mover(10, ventana)
        self.dictFiguras['personaje'].mover()
        
