class Autores:
    def __init__(self, nome:str, nacionalidade:str ):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.prox = None
        self.ant = None


    def __str__(self) -> str:
        return f"Nome: {self.nome}"