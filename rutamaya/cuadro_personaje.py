from cuadro import Interfaz_Cuadro

class personaje_niña(Interfaz_Cuadro):
    def __init__(self):
       Interfaz_Cuadro.__init__(self)

    def saludar(self):
       print("ooooo")
    
    def dibujar(self):
        self.image = pygame.image.load("rutamaya/personaje2.png").convert
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        

class prueba():
    print("hola")
#cuadropersonaje = Interfaz_Cuadro()
#cuadropersonaje.saludar()
#print("funcione puto")


'''
class cuadropersonaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("personaje2.png").convert
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
'''