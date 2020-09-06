from ruta.figuras import *
from ruta.verificacion import *
import math

class Solapamiento:

    _visibilidadOpcion = None

    def __init__(self, umbral, verificacion):
        self.umbral = umbral
        self.verificacion = verificacion
        self.posicionOpcion = None
        
    def verificar(self, posicionJugador):
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