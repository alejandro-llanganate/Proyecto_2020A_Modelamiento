import pygame
from ruta.obstaculos import *
from abc import ABC, abstractmethod

class FabricaObstaculos:
    @abstractmethod
    def crearObstaculo(self):
        pass

class FabricaObstaculoA(FabricaObstaculos):
    def crearObstaculo(self):
        return ObstaculoA()

class FabricaObstaculoB(FabricaObstaculos):
    def crearObstaculo(self):
        return ObstaculoB()
        
class FabricaObstaculoC(FabricaObstaculos):
    def crearObstaculo(self):
        return ObstaculoB()