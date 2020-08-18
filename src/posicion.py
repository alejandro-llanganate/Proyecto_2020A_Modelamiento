class Posicion:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def getPosicion(self):
        return self.x, self.y

    def actualizarX(self, nuevoX):
        self.x = nuevoX

    def actualizarY(self, nuevoY):
        self.y = nuevoY
