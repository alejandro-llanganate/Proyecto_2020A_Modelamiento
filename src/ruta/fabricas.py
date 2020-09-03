import pygame
from ruta.obstaculos import *
from abc import ABC, abstractmethod

class FabricaObstaculos:
    @abstractmethod
    def crearObstaculo(self):
        pass

class FabricaObstaculoA(FabricaObstaculos):
    def crearObstaculo(self, imagen, posicion):
        return ObstaculoA(imagen, posicion)

class FabricaObstaculoB(FabricaObstaculos):
    def crearObstaculo(self, imagen, posicion):
        return ObstaculoA(imagen, posicion)
        
