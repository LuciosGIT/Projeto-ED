from Node import Node


class LinkedList:

    """Lista encadeada simples para armazenar elementos dinamicamente."""
    def __init__(self):
        self.head = None
    
    def insert_end(self, data):
        """
        Insere um elemento no final da lista.

        Args:
            data: Elemento a ser inserido.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, value):
        """
        Busca um elemento na lista.

        Args:
            value: Valor a ser buscado.
            attr: (Opcional) Atributo do objeto a ser comparado.

        Returns:
            O elemento encontrado ou None se não existir.
        """
        current = self.head
        while current:
            if current.data == value:
                return current.data
            current = current.next
        return None
    
    def __repr__(self):
        
        """Representação textual da lista encadeada."""
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return " -> ".join(result)
    
    def values(self):
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result

ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print(ll)  # 10 -> 20 -> 30

print(ll.search(20))  # 20
print(ll.search(40))  # None
