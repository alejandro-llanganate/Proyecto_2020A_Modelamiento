import pygame
import sys
from cuadro import Interfaz_Cuadro
from cuadro_personaje import personaje_niña
from pygame.locals import *

blanco = (255, 255, 255)
negro = (0, 0, 0)
naranja = (231, 55, 18)


def comenzar():
    pygame.init()
    size = (850, 520)
    ventana = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    vida_personaje = 0

    personaje = pygame.image.load("personaje2.png")
    personaje.set_colorkey([0, 0, 0])  # retirar fondo

    # personaje = personaje_niña().dibujar()  #Ya no porque toca mandar el método blit

    piramide = pygame.image.load("rutamaya/piramide3.png").convert()
    piramide.set_colorkey([0, 0, 0])

    pregunta = pygame.image.load("rutamaya/pregunta4.png").convert()
    pregunta.set_colorkey([0, 0, 0])

    adorno_maya = pygame.image.load("rutamaya/adorno1.png").convert()
    adorno_maya.set_colorkey([0, 0, 0])

    fondo = pygame.image.load("rutamaya/fondo1.png").convert()
    fondo.set_colorkey([0, 0, 0])

    fondo_bienvenida = pygame.image.load("rutamaya/fondoBienvenida.png").convert()
    fondo_bienvenida.set_colorkey([0, 0, 0])

    boton_jugar

    rutamaya_inciada = True
    pantalla_bienvenido = True

    pygame.mouse.set_visible(False)  # ocultación puntero mouse



    while rutamaya_inciada:

        while pantalla_bienvenido:
            ventana.fill(blanco)
            ventana.blit(fondo_bienvenida, [0, 0])
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    print("escucheee")
                    pantalla_bienvenido = False

        ventana.fill(blanco)
        ventana.blit(fondo, [0, 0])
        posicion_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print("escucheee")
                bienvenido = False
                print(pantalla_bienvenido)

        ventana.fill(blanco)
        ventana.blit(fondo, [0, 0])
        print(posicion_mouse)
        x = posicion_mouse[0]
        y = posicion_mouse[1]

        for i in range(250, 700, 180):
            # pygame.draw.rect(ventana,negro,(i,300,50,50))
            ventana.blit(pregunta, [i, 380])

            # dibujando
            # pygame.draw.line(ventana, naranja, [15,85], [35,85], 8)
            # pygame.draw.rect(ventana,naranja,(200,150,100,50)) # inicio ancho alto

        ventana.blit(personaje, [x, y])
        ventana.blit(piramide, [82, 192])

        pygame.display.flip()  # podría ser método actualizar
        clock.tick(60)


comenzar()


class cuadropersonaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("personaje2.png").convert
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
