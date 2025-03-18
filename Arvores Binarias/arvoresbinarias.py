class No:
    """Classe que representa um nó da árvore binária."""
    def __init__(self, valor):
        self.valor = valor  # Valor armazenado no nó
        self.esquerda = None  # Referência para o nó da esquerda
        self.direita = None  # Referência para o nó da direita


class ArvoreBinaria:
    """Classe que representa uma Árvore Binária de Busca (BST)."""
    def __init__(self):
        self.raiz = None  # Inicialmente, a árvore está vazia

    def inserir(self, valor):
        """Insere um valor na árvore mantendo a ordem de busca."""
        if self.raiz is None:
            self.raiz = No(valor)  # Se a árvore está vazia, define a raiz
        else:
            self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, atual, valor):
        """Função auxiliar para inserir um nó recursivamente."""
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = No(valor)  # Insere à esquerda se não houver nó
            else:
                self._inserir_rec(atual.esquerda, valor)  # Continua descendo
        elif valor > atual.valor:
            if atual.direita is None:
                atual.direita = No(valor)  # Insere à direita se não houver nó
            else:
                self._inserir_rec(atual.direita, valor)  # Continua descendo

    def em_ordem(self):
        """Percorre a árvore em ordem e exibe os valores."""
        self._em_ordem_rec(self.raiz)
        print()

    def _em_ordem_rec(self, atual):
        """Percorre a árvore de forma recursiva (esquerda, raiz, direita)."""
        if atual is not None:
            self._em_ordem_rec(atual.esquerda)
            print(atual.valor, end=" ")
            self._em_ordem_rec(atual.direita)


# Exemplo de uso da Árvore Binária de Busca
arvore = ArvoreBinaria()
valores = [50, 30, 70, 20, 40, 60, 80]
for v in valores:
    arvore.inserir(v)

print("Elementos da árvore em ordem:")
arvore.em_ordem()  # Saída esperada: 20 30 40 50 60 70 80