class Product:
    """Representa um produto do supermercado."""

    
    def __init__(self, code, name, price):
        """
        Inicializa um produto.

        Args:
            code: Código identificador do produto.
            name: Nome do produto.
            price: Preço do produto.
        """
        self.code = code
        self.name = name
        self.price = price
    
    def __repr__(self):
        """Representação textual do produto."""
        return f"{self.code} - {self.name} (${self.price:.2f})"