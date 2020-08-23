import pygame
from assets.settings import *


pygame.init()


screen = pygame.display.set_mode(settings["tamañoVentana"])


myfont = pygame.font.SysFont("monospace", 15)

# render text
score = 5

start_ticks = pygame.time.get_ticks()  # starter tick


while True:  # mainloop
    myfont = pygame.font.SysFont("arial", 60)
    seconds = (pygame.time.get_ticks()-start_ticks) / 1000
    if seconds <= 1.0:
        label = myfont.render("3", 1, (255, 255, 255))
        screen.blit(label, (100, 100))
        print(3)
    if seconds <= 2.0 and seconds > 1.0:
        screen.fill((0, 0, 0))
        label = myfont.render("2", 1, (255, 255, 255))
        screen.blit(label, (100, 100))
        print(2)
    if seconds <= 3.0 and seconds > 2.0:
        screen.fill((0, 0, 0))
        label = myfont.render("1", 1, (255, 255, 255))
        screen.blit(label, (100, 100))
        print(1)
    if seconds <= 4.0 and seconds > 3:
        screen.fill((0, 0, 0))
        label = myfont.render("GO", 1, (255, 255, 255))
        screen.blit(label, (100, 100))
        print("GO")
        screen.fill((0, 0, 0))

    pygame.display.update()
