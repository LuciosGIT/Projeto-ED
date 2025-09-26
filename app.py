import streamlit as st
import pandas as pd
from datetime import datetime

from Node import Node
from LinkedList import LinkedList  
from Queue import Queue
from Supermarket import Supermarket
from Product import Product
from Customer import Customer


class ProductWithStock(Product):
    def __init__(self, code, name, price, quantity=0):
        super().__init__(code, name, price)
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name} (#{self.code}) - R${self.price:.2f} - Qtd: {self.quantity}"


class CustomerWithExtras(Customer):
    def __init__(self, name):
        super().__init__(name)
        self.timestamp = datetime.now()
        self.quantities = {}  
    
    def add_product_with_quantity(self, product, quantity):
        for _ in range(quantity):
            self.add_product(product)
        self.quantities[product.code] = self.quantities.get(product.code, 0) + quantity
    
    def get_cart_items(self):
        """Retorna lista de itens únicos com quantidades"""
        items = []
        product_counts = {}
        
        for product in self.cart.values():
            if product.code not in product_counts:
                product_counts[product.code] = {"product": product, "quantity": 0}
            product_counts[product.code]["quantity"] += 1
        
        return list(product_counts.values())
    
    def get_cart_count(self):
        """Retorna número total de itens únicos"""
        return len(set(p.code for p in self.cart.values()))
    
    def __str__(self):
        return f"{self.name} - R${self.total_value():.2f} - {self.get_cart_count()} tipos de itens"


def get_queue_list(queue):
    """Função auxiliar para obter lista da fila sem modificá-la"""
    result = []
    current = queue.first
    while current:
        result.append(current.data)
        current = current.next
    return result


if 'supermarket' not in st.session_state:
    st.session_state.supermarket = Supermarket()

    st.session_state.supermarket.add_product(ProductWithStock("001", "Arroz 5kg", 25.90, 100))
    st.session_state.supermarket.add_product(ProductWithStock("002", "Feijão 1kg", 8.50, 50))
    st.session_state.supermarket.add_product(ProductWithStock("003", "Açúcar 1kg", 4.20, 75))
    st.session_state.supermarket.add_product(ProductWithStock("004", "Óleo de Soja", 6.80, 30))
    st.session_state.supermarket.add_product(ProductWithStock("005", "Macarrão 500g", 3.50, 120))


st.title("🛒 Sistema de Supermercado")
st.sidebar.title("Menu")


menu_option = st.sidebar.selectbox(
    "Escolha uma opção:",
    ["📊 Dashboard", "📦 Gerenciar Produtos", "👥 Fila de Atendimento", "🛍️ Simular Compra"]
)

supermarket = st.session_state.supermarket


if menu_option == "📊 Dashboard":
    st.header("Dashboard do Supermercado")
    
    col1, col2, col3 = st.columns(3)
    
    products = supermarket.inventory.values()
    queue_customers = get_queue_list(supermarket.checkout_queue)
    
    with col1:
        st.metric("Total de Produtos", len(products))
    
    with col2:
        st.metric("Clientes na Fila", len(queue_customers))
    
    with col3:
        total_inventory_value = sum(p.price * p.quantity for p in products)
        st.metric("Valor Total Estoque", f"R$ {total_inventory_value:,.2f}")
    

    if products:
        st.subheader("Estoque por Produto")
        df_products = pd.DataFrame([
            {"Produto": p.name, "Quantidade": p.quantity, "Valor Unitário": p.price}
            for p in products
        ])
        st.bar_chart(df_products.set_index("Produto")["Quantidade"])

elif menu_option == "📦 Gerenciar Produtos":
    st.header("Gerenciamento de Produtos")
    
    tab1, tab2, tab3 = st.tabs(["➕ Adicionar Produto", "🔍 Buscar Produto", "📋 Lista de Produtos"])
    
    with tab1:
        st.subheader("Adicionar Novo Produto")
        with st.form("add_product_form"):
            code = st.text_input("Código do Produto")
            name = st.text_input("Nome do Produto")
            price = st.number_input("Preço", min_value=0.01, step=0.01)
            quantity = st.number_input("Quantidade", min_value=0, step=1)
            
            if st.form_submit_button("Adicionar Produto"):
                if code and name:
                
                    existing = supermarket.find_product(code)
                    if existing:
                        st.error("Produto com este código já existe!")
                    else:
                        product = ProductWithStock(code, name, price, quantity)
                        supermarket.add_product(product)
                        st.success(f"Produto '{name}' adicionado com sucesso!")
                else:
                    st.error("Preencha todos os campos obrigatórios!")
    
    with tab2:
        st.subheader("Buscar Produto")
        search_code = st.text_input("Digite o código do produto:")
        if search_code:
            product = supermarket.find_product(search_code)
            if product:
                st.success("Produto encontrado!")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Nome:** {product.name}")
                    st.write(f"**Código:** {product.code}")
                with col2:
                    st.write(f"**Preço:** R$ {product.price:.2f}")
                    st.write(f"**Quantidade:** {product.quantity}")
            else:
                st.error("Produto não encontrado!")
    
    with tab3:
        st.subheader("Lista Completa de Produtos")
        products = supermarket.inventory.values()
        if products:
            df = pd.DataFrame([
                {
                    "Código": p.code,
                    "Nome": p.name,
                    "Preço": f"R$ {p.price:.2f}",
                    "Quantidade": p.quantity,
                    "Valor Total": f"R$ {p.price * p.quantity:.2f}"
                }
                for p in products
            ])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Nenhum produto cadastrado.")


elif menu_option == "👥 Fila de Atendimento":
    st.header("Fila de Atendimento")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Fila Atual")
        queue_customers = get_queue_list(supermarket.checkout_queue)
        
        if queue_customers:
            for i, customer in enumerate(queue_customers, 1):
                with st.expander(f"{i}º - {customer.name} (R$ {customer.total_value():.2f})"):
                    st.write(f"**Cliente:** {customer.name}")
                    st.write(f"**Horário de Entrada:** {customer.timestamp.strftime('%H:%M:%S')}")
                    st.write(f"**Total da Compra:** R$ {customer.total_value():.2f}")
                    st.write(f"**Tipos de Produtos:** {customer.get_cart_count()}")
                    
                    cart_items = customer.get_cart_items()
                    if cart_items:
                        st.write("**Produtos:**")
                        for item in cart_items:
                            st.write(f"- {item['product'].name} x{item['quantity']} = R$ {item['product'].price * item['quantity']:.2f}")
        else:
            st.info("Nenhum cliente na fila.")
    
    with col2:
        st.subheader("Atender Cliente")
        if st.button("🔔 Chamar Próximo Cliente", type="primary"):
            customer = supermarket.serve_customer()
            if customer:
                st.success(f"Atendendo: {customer.name}")
                st.write(f"Total: R$ {customer.total_value():.2f}")
                st.balloons()
            else:
                st.warning("Nenhum cliente na fila!")


elif menu_option == "🛍️ Simular Compra":
    st.header("Simular Processo de Compra")
    
    with st.form("customer_form"):
        st.subheader("Dados do Cliente")
        customer_name = st.text_input("Nome do Cliente")
        
        st.subheader("Adicionar Produtos ao Carrinho")
        products = supermarket.inventory.values()
        
        if products:
            selected_products = st.multiselect(
                "Selecione os produtos:",
                options=products,
                format_func=lambda x: f"{x.name} - R$ {x.price:.2f}"
            )
            
            quantities = {}
            for product in selected_products:
                quantities[product.code] = st.number_input(
                    f"Quantidade de {product.name}:",
                    min_value=1,
                    max_value=product.quantity,
                    value=1,
                    key=f"qty_{product.code}"
                )
        
        if st.form_submit_button("🛒 Adicionar à Fila"):
            if customer_name and selected_products:
                customer = CustomerWithExtras(customer_name)
                
                for product in selected_products:
                    quantity = quantities[product.code]
                    customer.add_product_with_quantity(product, quantity)
                  
                    product.quantity -= quantity
                
                supermarket.add_customer(customer)
                st.success(f"Cliente {customer_name} adicionado à fila!")
                st.write(f"Total da compra: R$ {customer.total_value():.2f}")
                st.rerun()
            else:
                st.error("Preencha o nome do cliente e selecione pelo menos um produto!")


st.sidebar.markdown("---")
st.sidebar.markdown("**Desenvolvido com:**")
st.sidebar.markdown("- LinkedList (Lista Ligada)")
st.sidebar.markdown("- Queue (Fila)")
st.sidebar.markdown("- Streamlit")