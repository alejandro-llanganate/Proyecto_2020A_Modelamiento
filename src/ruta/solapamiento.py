from ruta.figuras import *
import math

class SolapamientoRuta:
    def __init__(self, umbral):
        self.umbral = umbral
        self.posicionOpcion = None
        
    def verificar(self, posicionJugador):
        if self.posicionOpcion != None:
            (x1, y1) = posicionJugador
            (x2, y2) = self.posicionOpcion
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2))
            if distancia <= self.umbral:
                print("solapamiento chugcha")
    
    def actualizar(self, posicionOpcion):
        self.posicionOpcion = posicionOpcion


                

    



