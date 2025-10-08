class Node:
    """Classe que representa um nó de uma lista encadeada."""


    def __init__(self, data):
        """
        Inicializa um nó da lista.

        Args:
            data: Valor armazenado no nó.
        """
        self.data = data
        self.next = None
