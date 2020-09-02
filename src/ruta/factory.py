import pygame
from abc import ABC, abstractmethod
from ruta.obstaculo import *

class FabricaObstaculo:
    def __init__(self):
        #self.tipoObstaculo = tipoObstaculo


    @abstractmethod
    def crearObstaculo(self):
        pass

class FabricaObstaculoA(self):
    def __init__(self):
        pass

    def crearObstaculo(self, imagen, posicion):
        if(self.tipoObstaculo == "A"):
            return ObstaculoA(imagen, posicion)