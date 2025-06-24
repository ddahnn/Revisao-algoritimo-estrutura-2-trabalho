class Pilha:
    class Node:
        def __init__(self, livro):
            self.livro = livro
            self.prox = None

    def __init__(self):
        self.topo = None

    def add(self, livro):
        novo_node = self.Node(livro)
        novo_node.prox = self.topo
        self.topo = novo_node
        print("Livro adicionado à pilha.")

    def exibir_lista(self):
        if self.topo is None:
            print("A pilha está vazia.")
            return

        atual = self.topo
        print("Pilha de Livros:")
        while atual:
            print(atual.livro)
            atual = atual.prox


    def remover_livro(self):
        if self.topo is None:
            print("A lista esta vazia")
        item_removido = self.topo
        self.topo = self.topo.prox
        print(f"O item {item_removido.livro}, foi removido")
        return item_removido.livro