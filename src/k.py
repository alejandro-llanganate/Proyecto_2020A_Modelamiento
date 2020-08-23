import pygame
from assets.settings import *


pygame.init()


screen = pygame.display.set_mode(settings["tamañoVentana"])


myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Some text!", 1, (0, 0, 0))
score = 5

start_ticks = pygame.time.get_ticks()  # starter tick
while True:  # mainloop
    
    
    
    
    seconds = (pygame.time.get_ticks()-start_ticks) / 1000
    if seconds == 1.0:
        print(3)
    if seconds == 2.0:
        print(2)
    if seconds == 3.0:
        print(1)
    if seconds == 4.0:
        print("Go")

    pygame.display.update()
