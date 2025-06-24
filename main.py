from modules.Livro import Livro
from modules.Autor import Autores
from services.livros_Services import Pilha

# Criando autores
autor1 = Autores("Machiavelli", "Italiana")
autor2 = Autores("Friedrich Nietzsche", "Alemã")

# Criando livros
livro1 = Livro("Livro A", autor1, 100)
livro2 = Livro("Livro B", autor1, 200)
livro3 = Livro("Livro C", autor2, 300)

# Criando pilha
pilha = Pilha()

# Adicionando livros
pilha.add(livro1)
pilha.add(livro2)
pilha.add(livro3)

# Exibindo pilha
pilha.exibir_lista()


pilha.remover_livro()

# Exibindo pilha
pilha.exibir_lista()