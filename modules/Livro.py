from .Autor import Autores
class Livro:
    def __init__(self, titulo: str, autor: Autores, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.inicio = None
        self.prox = None

    def __str__(self)  -> str:
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Paginas: {self.paginas}"
        