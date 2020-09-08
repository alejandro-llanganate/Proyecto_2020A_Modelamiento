from ruta.figuras import *
from ruta.verificacion import *
import math

class Solapamiento():
    @abstractmethod
    def verificarSolapamiento(self):
        pass

class SolapamientoConOpcion(Solapamiento):

    _visibilidadOpcion = None

    def __init__(self, umbral, verificacion):
        self.umbral = umbral
        self.verificacion = verificacion
        self.posicionOpcion = None
        
    def verificarSolapamientoOpcion(self, posicionJugador):
        if self.posicionOpcion != None and self._visibilidadOpcion == True:
            (x1, y1) = posicionJugador
            (x2, y2) = self.posicionOpcion
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
            if distancia <= self.umbral:
                self.verificacion.verificarSeleccion(self.letraSeleccionada)
    
    def actualizar(self, posicionOpcion, visibilidad, letra):
        self.letraSeleccionada = letra
        self.posicionOpcion = posicionOpcion
        self._visibilidadOpcion = visibilidad

class SolapamientoConObstaculo(Solapamiento):
    def __init__(self, umbral, verificacion, camino):
        self.umbral = umbral
        self.verificacion = verificacion
        self.posicionObstaculo = None
        self.camino = camino
    
    def verificarSolapamiento(self, posicionPersonaje):
        (x1, y1) = posicionPersonaje
        for obstaculo in self.camino.obtenerObstaculos():
            (x2, y2) = obstaculo.posicion.getPosicion()
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
            if distancia <= self.umbral:
                self.verificacion.notificarSolapamiento(True)
                obstaculo.posicion.actualizarY(settings["tamañoVentana"][1])
            else:
                self.verificacion.notificarSolapamiento(False)