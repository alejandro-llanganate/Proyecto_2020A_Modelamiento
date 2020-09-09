import pygame
from abc import ABC, abstractmethod
from ruta.assets.herramientas import *
from ruta.assets.settings import *
from ruta.listener import *
from ruta.audioPregunta import *
from ruta.solapamiento import *
from ruta.fabricas import *


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

    _i = 0
    _iteradorAudioPregunta = -1

    def __init__(self, imagen, posicion, playlist):
        super().__init__(posicion)
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(
            self.imagen, settings["tamañoCamino"])
        self.estadoMovimiento = True
        self.obs = FabricaRandomica().crearObstaculo()
        self.playlist = playlist
        
    def dibujar(self, ventana):
        posicion = self.posicion.getPosicion()
        ventana.blit(self.imagen, (posicion[0], settings["tamañoCamino"][1]))
        

    def mover(self, ventana, opciones):
        if(self.estadoMovimiento and self._iteradorAudioPregunta < 3):
            x, y = self.posicion.getPosicion()
            alturaImagen = self.imagen.get_rect().height
            relativoY = y % alturaImagen
            self.distancia = abs(y)
            if(self.distancia <= alturaImagen*3):
                ventana.blit(self.imagen, (x, relativoY - alturaImagen))
                if relativoY < settings['tamañoVentana'][1]:
                    ventana.blit(self.imagen, (x, relativoY))
                self.posicion.actualizarY(y-settings["factorDesplazamiento"])

                escogido = self.obs[self._i]
                escogido.dibujar(ventana)
                escogido.mover()
                if escogido.posicion.getPosicion()[1] < 0:
                    self._i += 1
                    escogido = self.obs[self._i]
                    escogido.dibujar(ventana)
                    escogido.mover()
                if escogido.posicion.getPosicion()[1] < 0 and self._i==1:
                    self._i += 1
                    escogido = self.obs[self._i]
                    escogido.dibujar(ventana)
                    escogido.mover()
            else:
                self.estadoMovimiento = False
                self.posicion.actualizarY(0)
                self._iteradorAudioPregunta += 1
                
        else:
            self.playlist.obtenerAudiosPreguntas()[self._iteradorAudioPregunta].reproducir(self.notificar(), opciones)
            ventana.blit(self.imagen, settings["coordenadaCamino"])

        if (self._iteradorAudioPregunta > 3):
            self._i=0

    
    def obtenerObstaculos(self):
        return self.obs

    def notificar(self):
        if(self.estadoMovimiento == False):
            return self.estadoMovimiento
    
    def setEstadoMovimiento(self, valor):
        self.estadoMovimiento = valor

    def getEstado(self):
        return self.estadoMovimiento

    def reiniciarIteradores(self):
        self._i=0
        self._iteradorAudioPregunta=-1
        self.posicion.actualizarY(0)
        self.obs = FabricaRandomica().crearObstaculo()
        for audio in self.playlist.obtenerAudiosPreguntas():
            audio.setEstadoReproducido(True)


class Personaje(Figura):
    def __init__(self, imagen, posicion, solapamientoConOpcion, solapamientoConObstaculo):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoPersonaje"])
        self.solapamientoConOpcion = solapamientoConOpcion
        self.solapamientoConObstaculo = solapamientoConObstaculo
        super().__init__(posicion)


    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        x, y = Listener.captarMouse()
        tamañoImagen = self.imagen.get_rect()
        distanciaVereda = (settings["tamañoVentana"][0] - settings["tamañoCamino"][0])/2
        condicionLimiteX = x >= distanciaVereda and x <= settings["tamañoVentana"][0] - distanciaVereda
        condicionLimiteY = y >= settings["tamañoVentana"][1] * 0.1 and y <= settings["tamañoVentana"][1]*0.9
        if(condicionLimiteX and condicionLimiteY):
            self.posicion.actualizarX(Listener.captarMouse()[0]-tamañoImagen.width/2)
            self.posicion.actualizarY(Listener.captarMouse()[1]-tamañoImagen.height/2)
        for solapamiento in self.solapamientoConOpcion:
            solapamiento.verificarSolapamiento(self.posicion.getPosicion())  
        self.solapamientoConObstaculo.verificarSolapamiento(self.posicion.getPosicion())


class FiguraVida(Figura):
    def __init__(self, posicion):
        self.imagen = None
        self.posicion = posicion
        self.numeroVidas = 4

    def dibujar(self, ventana):
        if(self.numeroVidas == 4):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida4.png', __file__))
        elif (self.numeroVidas == 3):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida3.png', __file__))
        elif (self.numeroVidas == 2):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida2.png', __file__))
        elif (self.numeroVidas == 1):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida1.png', __file__))
        else:
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida0.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoFigVida"])
        ventana.blit(self.imagen, self.posicion.getPosicion())
    
    def disminuirVidas(self):
        self.numeroVidas = self.numeroVidas - 1

    def obtenerNumeroVidas(self):
        return self.numeroVidas

    def mover(self):
        pass

    def reiniciarNumeroDeVidas(self):
        self.numeroVidas = 4




class FiguraOpcion(Figura):
    def __init__(self, imagen, posicion, letraAsociada, solapamiento):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoOpcion"])
        self.posicion = posicion
        self.letraAsociada = letraAsociada
        self.solapamiento = solapamiento
        self.visibilidad = False

    def dibujar(self, ventana):
        if(self.visibilidad == True):
            ventana.blit(self.imagen, self.posicion.getPosicion())

    def setVisibilidad(self, esVisible):
        self.visibilidad = esVisible

    def mover(self):
        pass

    def getPosicion(self):
        self.posicion.getPosicion()

    def notificar(self):
        self.solapamiento.actualizar(self.posicion.getPosicion(), self.visibilidad, self.getLetraAsociada())

    def getLetraAsociada(self):
        return self.letraAsociada

    def obtenerVisibilidad(self):
        return self.visibilidad


class Marcador(Figura):
    def __init__(self, imagen, posicion, puntaje):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoMarcador"])
        self.posicion = posicion
        self.puntaje = puntaje

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())
        fuente = pygame.font.SysFont('comicsansms', settings["tamañoLetraPuntaje"])
        textoPuntaje = fuente.render(f'Puntaje: {self.puntaje.getPuntos()}', True, (255, 255, 255))
        ventana.blit(textoPuntaje, (self.posicion.getPosicion()[0]*1.065, self.posicion.getPosicion()[1]*1.3))
        
    def subirPuntajeMarcador(self):
        return puntaje.aumentar()

    def mover(self):
        pass


class Mapa(Figura):
    def __init__(self):
        self.listaFiguras = []

    def agregarFigura(self, figura):
        self.listaFiguras.append(figura)

    def quitarFigura(self):
        self.listaFiguras.remove(figura)

    def dibujar(self, ventana):
        for figura in self.listaFiguras:
            figura.dibujar(ventana)
            if isinstance(figura, FiguraOpcion):
                figura.notificar() 

    def mover(self, ventana):
        for figura in self.listaFiguras:
            if isinstance(figura, Camino):
                figura.mover(ventana, list(filter(lambda e: isinstance(e, FiguraOpcion), self.listaFiguras)))
            elif isinstance(figura, Personaje):
                figura.mover()
        pygame.mouse.set_visible(False)

    def obtenerOpciones(self):
        return filter(lambda e: isinstance(e, FiguraOpcion), self.listaFiguras)
    
    def actualizar(self, comprobacion):
        for figura in self.listaFiguras:
            if isinstance(figura, Camino):
                figura.setEstadoMovimiento(True)
            elif isinstance(figura, FiguraOpcion):
                figura.setVisibilidad(False)
            elif comprobacion == False and isinstance(figura, FiguraVida):
                figura.disminuirVidas()
        
    def obtenerVidasActuales(self):
        return list(filter(lambda e: isinstance(e, FiguraVida), self.listaFiguras))[0].obtenerNumeroVidas()
    
    def obtenerFiguraVida(self):
        return list(filter(lambda e: isinstance(e, FiguraVida), self.listaFiguras))[0]
    
    def obtenerCamino(self):
        return list(filter(lambda e: isinstance(e, Camino), self.listaFiguras))[0]
