import pygame
import os
import sys
sys.path.append('../juego.py')
from juego import *


class Snake(Juego):
    def __init__(self):
        self.dimensiones = (714,476)
        self.titulo = 'Snake'
        self.ventana = None
        self.imagen = pygame.image.load(os.path.join(os.path.dirname(__file__),'img/inicioSnake.png'))
        self.clock = pygame.time.Clock()

    def iniciarJuego(self):
        self.ventana = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)
        bandera=True
        while bandera:
            self.clock.tick(30)
            self.ventana.blit(self.imagen, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
                    pygame.quit()

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
