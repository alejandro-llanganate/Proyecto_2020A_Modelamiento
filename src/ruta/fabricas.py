import pygame
import random
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
        return ObstaculoC()

class FabricaRandomica2(FabricaObstaculos):
    def crearObstaculo(self):
        listaObstaculos = []
        for i in range (4):
            aleatorio = random.randrange(1,4)
            if aleatorio == 1:
                obstaculo = ObstaculoA()
                listaObstaculos.append(obstaculo)
            elif aleatorio == 2:
                obstaculo = ObstaculoB()
                listaObstaculos.append(obstaculo)
            elif aleatorio == 3:
                obstaculo = ObstaculoC()
                listaObstaculos.append(obstaculo)
        return listaObstaculos
    