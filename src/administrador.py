from repositorio import *

class Administrador:
    def __init__(self, numeroPreguntas):
        self.numeroPreguntas = numeroPreguntas
        self.repositorio = RepositorioCuestionario()
    
    def cargarContenidoPregunta(self):
        contenido = f'''
        {self.repositorio.obtenerPregunta()["pregunta"]}
        a) X
        b) R
        c) Y
        '''
        return contenido