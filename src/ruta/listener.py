import pygame
from ruta.listener import *

class Listener:
    @staticmethod
    def captarMouse():
        return pygame.mouse.get_pos()
