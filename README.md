# 🛒 Sistema de Supermercado

## 📝 Descrição

Sistema de gerenciamento de supermercado desenvolvido como projeto acadêmico para a disciplina de **Estrutura de Dados**. O sistema implementa estruturas de dados fundamentais como **Lista Ligada** (LinkedList) e **Fila** (Queue) para gerenciar produtos e atendimento de clientes.

## 🎯 Funcionalidades

### 📦 Gerenciamento de Produtos
- ➕ Adicionar novos produtos ao estoque
- 🔍 Buscar produtos por código
- 📋 Visualizar lista completa de produtos
- 💰 Controle de preços e quantidades

### 👥 Sistema de Fila de Atendimento
- 🛍️ Adicionar clientes à fila de checkout
- ⏭️ Atender clientes seguindo ordem FIFO (First In, First Out)
- 👀 Visualizar fila atual com detalhes dos carrinhos
- 📊 Acompanhar tempo de espera

### 🖥️ Interface Web Interativa
- 📊 Dashboard com métricas do supermercado
- 🎮 Simulação completa do processo de compra
- 📈 Gráficos de estoque
- 💻 Interface moderna e responsiva

## 🏗️ Estrutura do Projeto

```
supermercado/
│
├── Node.py              # Classe Node para estruturas de dados
├── LinkedList.py        # Implementação da Lista Ligada
├── Queue.py            # Implementação da Fila
├── Supermarket.py      # Classe principal do supermercado
├── Product.py          # Classe do produto
├── Customer.py         # Classe do cliente
├── app.py             # Interface Streamlit
├── README.md          # Documentação do projeto
└── requirements.txt   # Dependências do projeto
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** - Linguagem principal
- **Estruturas de Dados Customizadas:**
  - Lista Ligada (LinkedList)
  - Fila (Queue)
  - Nós (Node)
- **Streamlit** - Interface web interativa
- **Pandas** - Manipulação e visualização de dados

## ⚙️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd supermercado
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows (PowerShell):**
```bash
.\venv\Scripts\activate
```

**Windows (CMD):**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install streamlit pandas
```

### 5. Execute a aplicação
```bash
streamlit run app.py
```

## 🚀 Como Usar

### 1. **Dashboard**
- Visualize métricas gerais do supermercado
- Acompanhe total de produtos, clientes na fila e valor do estoque
- Veja gráfico de distribuição de estoque

### 2. **Gerenciar Produtos**
- **Adicionar:** Cadastre novos produtos com código, nome, preço e quantidade
- **Buscar:** Encontre produtos específicos pelo código
- **Listar:** Visualize todos os produtos em formato de tabela

### 3. **Fila de Atendimento**
- Visualize todos os clientes na fila de espera
- Veja detalhes do carrinho de cada cliente
- Atenda clientes seguindo a ordem de chegada (FIFO)

### 4. **Simular Compra**
- Crie um novo cliente
- Adicione produtos ao carrinho
- Cliente é automaticamente adicionado à fila de checkout

## 🏛️ Arquitetura das Estruturas de Dados

### 📋 Lista Ligada (LinkedList)
- Armazena o inventário de produtos
- Permite inserção no final e busca por critérios
- Implementa iteração personalizada

### 🚶‍♂️ Fila (Queue)
- Gerencia fila de atendimento dos clientes
- Segue princípio FIFO (First In, First Out)
- Operações: `enqueue` (entrar na fila) e `dequeue` (sair da fila)

### 🔗 Nó (Node)
- Estrutura básica para LinkedList e Queue
- Contém dados e referência para próximo nó

## 📊 Exemplos de Uso

### Adicionar Produto
```python
supermarket = Supermarket()
produto = Product("001", "Arroz 5kg", 25.90)
supermarket.add_product(produto)
```

### Buscar Produto
```python
produto_encontrado = supermarket.find_product("001")
print(produto_encontrado)  # 001 - Arroz 5kg ($25.90)
```

### Gerenciar Fila de Clientes
```python
cliente = Customer("João Silva")
cliente.add_product(produto)
supermarket.add_customer(cliente)

# Atender próximo cliente
cliente_atendido = supermarket.serve_customer()
```

## 🎓 Conceitos de Estrutura de Dados Aplicados

- **Lista Ligada:** Armazenamento dinâmico de produtos
- **Fila (Queue):** Gerenciamento FIFO de clientes
- **Busca Linear:** Localização de produtos por código
- **Iteração:** Percorrer estruturas de dados customizadas
- **Encapsulamento:** Classes bem estruturadas e modulares

## 🤝 Contribuição

Este é um projeto acadêmico desenvolvido para fins educacionais. Contribuições são bem-vindas para melhorar a implementação das estruturas de dados ou adicionar novas funcionalidades.

## 📜 Licença

Este projeto é desenvolvido para fins acadêmicos e educacionais.

---

