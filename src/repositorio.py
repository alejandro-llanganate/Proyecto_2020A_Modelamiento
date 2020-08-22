import json
from assets.herramientas import *
import random


class Repositorio:
    def __init__(self):
        try:
            with open(obtenerPathAbsoluto('data/cuestionario.json', __file__)) as archivoJSON:
                self.__data = json.load(archivoJSON)
        except FileNotFoundError as error:
            print('No se encontró el archivo del cuestionario, error: ', error)

    def obtenerPregunta(self):
        return self.__data["preguntas"][random.randint(0, len(self.__data["preguntas"])-1)]


m = Repositorio()
print(m.obtenerPregunta())
