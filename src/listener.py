import pygame
from listener import *

pygame.init()


class Listener:
    @staticmethod
    def captarMouse():
        return pygame.mouse.get_pos()
