class Node:
    """
    Classe Node para listas encadeadas.
    Cada nó contém um valor (item) e uma referência para o próximo nó.
    """
    def __init__(self, item: any):
        self.item = item
        self.next = None

    def __repr__(self):
        return f"Node({self.item})"
     

class No:
    def __init__(self, dado):
        self.dado = dado  # Armazena o valor do nó
        self.prox = None  # Ponteiro para o próximo nó


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None  # Primeiro nó da lista
        self.ultimo = None    # Último nó da lista
        self.qtdNos = 0       # Contador de nós

    def insereFim(self, novo_no):
        """Insere um novo nó no final da lista."""
        novo_no.prox = None  # O novo nó sempre aponta para None (será o último)
        if self.primeiro is None:  # Se a lista estiver vazia
            self.primeiro = novo_no  # O novo nó será o primeiro nó
        else:
            self.ultimo.prox = novo_no  # O último nó atual aponta para o novo nó
        self.ultimo = novo_no  # O novo nó agora é o último
        self.qtdNos += 1  # Atualiza a contagem de nós

    def insereInicio(self, novo_no):
        """Insere um novo nó no início da lista."""
        novo_no.prox = self.primeiro  # O novo nó aponta para o primeiro nó atual
        if self.primeiro is None:  # Se a lista estiver vazia
            self.ultimo = novo_no  # O novo nó será também o último nó
        self.primeiro = novo_no  # O novo nó agora é o primeiro
        self.qtdNos += 1  # Atualiza a contagem de nós

    def inserePosicao(self, novo_no, pos):
        """Insere um novo nó em uma posição específica da lista."""
        if pos <= 0:  # Se a posição for menor ou igual a 0, insere no início
            self.insereInicio(novo_no)
        elif pos >= self.qtdNos:  # Se a posição for maior ou igual ao tamanho, insere no final
            self.insereFim(novo_no)
        else:
            aux = self.primeiro  # Começa no primeiro nó
            pos_aux = 1
            while pos_aux < pos:  # Percorre a lista até a posição desejada
                aux = aux.prox
                pos_aux += 1
            novo_no.prox = aux.prox  # O novo nó aponta para o próximo nó da posição
            aux.prox = novo_no  # O nó anterior aponta para o novo nó
            self.qtdNos += 1  # Atualiza a contagem de nós

    def contaNos(self):
        """Retorna o total de nós na lista."""
        tam = 0
        aux = self.primeiro
        while aux is not None:
            tam += 1
            aux = aux.prox
        return tam

    def exibeLista(self):
        """Exibe todos os elementos da lista encadeada."""
        aux = self.primeiro
        while aux is not None:
            print(aux.dado, end=" -> ")
            aux = aux.prox
        print("None")


# Testando a Lista Encadeada:
lista = ListaEncadeada()

lista.insereFim(No(10))   # Insere 10 no final
lista.insereInicio(No(5)) # Insere 5 no início
lista.inserePosicao(No(7), 1) # Insere 7 na posição 1
lista.insereFim(No(15))   # Insere 15 no final

lista.exibeLista()  # Saída esperada: 5 -> 7 -> 10 -> 15 -> None