from Node import Node

class Queue:
    """Fila simples implementada com nós encadeados."""
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, data):
        """
        Adiciona um elemento no final da fila.

        Args:
            data: Elemento a ser adicionado.
        """
        new_node = Node(data)
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
    
    def dequeue(self):
        """
        Remove e retorna o elemento do início da fila.

        Returns:
            O elemento removido ou None se a fila estiver vazia.
        """
        if not self.first:
            return None
        data = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data