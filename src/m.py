import pygame
from assets.herramientas import *
# --- class ---


class Button(object):

    def __init__(self, position, size):
        self._image = pygame.image.load(
            obtenerPathAbsoluto('img/botonJugar.png', __file__))
        self._image = pygame.transform.scale(self._image, size)
        self._rect = pygame.Rect(position, size)

    def draw(self, screen):
        # draw selected image
        screen.blit(self._image, self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self._rect.collidepoint(event.pos):  # is mouse over button
                    print("Hola mundo")

# --- main ---

# init


pygame.init()

screen = pygame.display.set_mode((320, 110))

# create buttons

button1 = Button((5, 5), (100, 100))
# mainloop

running = True

while running:

    # --- events ---

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # --- buttons events ---

        button1.event_handler(event)
    # --- draws ---

    button1.draw(screen)

    pygame.display.update()

# --- the end ---

pygame.quit()
