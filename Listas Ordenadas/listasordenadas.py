def insereOrdenado(self, novo_no):
    """Insere um nó mantendo a lista em ordem crescente."""
    if self.primeiro is None or novo_no.dado < self.primeiro.dado:
        # Se a lista estiver vazia ou o novo nó for menor que o primeiro
        novo_no.prox = self.primeiro
        self.primeiro = novo_no
        if self.ultimo is None:  # Caso a lista estivesse vazia
            self.ultimo = novo_no
    else:
        # Percorre a lista até encontrar a posição correta
        atual = self.primeiro
        while atual.prox is not None and atual.prox.dado < novo_no.dado:
            atual = atual.prox
        novo_no.prox = atual.prox
        atual.prox = novo_no
        if novo_no.prox is None:  # Se for inserido no final
            self.ultimo = novo_no
    self.qtdNos += 1
    