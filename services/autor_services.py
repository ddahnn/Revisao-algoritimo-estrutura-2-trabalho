from modules.Autor import Autores

class Lista_Ordenada:
    class Nodo:
        def __init__(self, autor):
            self.autor = autor
            self.prox = None
            self.ant = None

    def __init__(self):
        self.inicio = None


    def add (self, autor):
        nodo = 