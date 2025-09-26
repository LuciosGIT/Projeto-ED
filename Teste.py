from Supermarket import Supermarket
from Product import Product
from Customer import Customer

if __name__ == "__main__":
    mercado = Supermarket()

    # Adicionando produtos ao estoque
    mercado.add_product(Product(101, "Arroz", 20.50))
    mercado.add_product(Product(102, "Feijão", 8.90))
    mercado.add_product(Product(103, "Macarrão", 5.30))

    print("Estoque:", mercado.inventory)

    # Criando cliente e adicionando produtos
    cliente1 = Customer("Ana")
    cliente1.add_product(mercado.find_product(101))
    cliente1.add_product(mercado.find_product(103))

    mercado.add_customer(cliente1)

    # Atender cliente
    mercado.serve_customer()