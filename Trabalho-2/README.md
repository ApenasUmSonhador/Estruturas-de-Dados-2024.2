# **Trabalho 2**
## **Estrutura do Projeto**

A estrutura do projeto para o **Trabalho 1** segue a seguinte organização:
```yaml
Trabalho-2/
├── Questões_1_e_3/                # Pasta com questões 1 e 3
│   ├── __init__.py                # Arquivo principal que executa os testes
│   ├── setup_init_paths.py        # Configurador de paths para __init__.py
│   ├── Tests/                     # Pasta com testes automatizados 
│   │   ├── setup_paths.py         # Configurador de paths para os testes
│   │   ├── test_bst.py            # Testes relacionados à árvore binária de busca
│   │   ├── test_node.py           # Testes relacionados à nó
│   │   ├── test_product_bst.py    # Testes relacionados à árvore binária de busca modificada
│   │   ├── test_product_node.py   # Testes relacionados ao nó modificado
│   └── Classes/                   # Pasta com as implementações principais
│       ├── Bst.py                 # Implementação da estrutura de árvore binária de busca
│       ├── Node.py                # Implementação da estrutura de nó
│       ├── Product_bst.py         # Implementação do estrutura de árvore binária de busca modificada
│       ├── Product_node.py        # Implementação da estrutura de nó modificado
├── Questão_7.ipynb                # Resolução da questão 7 via jupyter notebook
├── Questão_9.ipynb                # Resolução da questão 9 via jupyter notebook
└── README.md                      # Documentação do projeto para Trabalho 2
```

---

## **Funcionalidades em Questões_1_e_3**

- **Classes/Bst.py**  
  Implementa estrutura de dados **árvore binária de busca** para atender às especificidades da questão 1

- **Classes/Node.py**  
  Implementa estrutura **nó** com `left`, `right` e `value`

- **Classes/Product_bst.py**  
  Implementa estrutura de dados **árvore binária de busca modificada** para atender às especificidades da questão 3
  
- **Classes/Product_node.py**  
  Implementa estrutura de dados **nó modificado** com `left`, `right`, `id` e `quantity`

  
- **Tests/Bst.py**  
  Contém testes automatizados para validar o desempenho e comportamento correto da classe `Bst`.

- **Tests/Node.py**  
  Contém testes automatizados para validar o desempenho e comportamento correto da classe `Node`.

- **Tests/Product_bst.py**  
  Contém testes automatizados para validar o desempenho e comportamento correto da classe `Product_bst`.
  
- **Tests/Product_node.py**  
  Contém testes automatizados para validar o desempenho e comportamento correto da classe `Product_node`.

---

## **Configuração**

1. Certifique-se de que o Python 3.8+ está instalado no sistema.  

2. Clone o repositório:

```bash
   git clone https://github.com/ApenasUmSonhador/Estruturas-de-Dados-2024.2.git
   cd Estruturas-de-Dados-2024.2/Trabalho-2/Questões_1_e_3
```

---

## **Como executar Questões_1_e_3**
### Rodar os testes
Para executar os testes automatizados diretamente, rode o seguinte comando na pasta Questões_1_e_3:

```bash
python __init__.py
```
Isso importará e executará os módulos de teste, garantindo que as implementações estejam funcionando corretamente.

---

### Utilização de `Node`

```python
from Classes.Node import Node

node = Node(13)
print(node)       # Saída esperada: "13"

# Linkando nós
node.left = Node(10)
node.right = Node(15)

print(node.left)  # Saída esperada: "10" 
print(node.right) # Saída esperada: "15"
```

### Operações com `Bst`
```python
from Classes.Bst import Bst

# Criação da árvore binária de busca
bst = Bst()

# Inserção de valores na árvore
bst.insert(10)
bst.insert(20)
bst.insert(5)

# Busca de valores na árvore
print(bst.search(10))       # Saída esperada: True
print(bst.search(15))       # Saída esperada: False

# Remoção de um valor da árvore
bst.remove(10)

# Verificação da altura da árvore
print(bst.height())         # Saída esperada: 2

# Percorrendo a árvore em ordem
print(bst.in_order())       # Saída esperada: [5, 20]

# Encontrando o valor máximo e mínimo
print(bst.get_max_value())  # Saída esperada: 20
print(bst.get_min_value())  # Saída esperada: 5
```
### Operações com `Product_bst`
```python
from Classes.Product_bst import Product_bst

# Criação da árvore binária de busca de produtos
product_bst = Product_bst()

# Inserção de produtos na árvore
product_bst.insert(101, 5)
product_bst.insert(102, 3)
product_bst.insert(103, 8)

# Busca de produtos na árvore
product = product_bst.search(101)
print(product)  # Saída esperada: p_id: 101 quantity: 5

# Remoção de um produto da árvore
product_bst.remove(102)

# Alteração da quantidade de um produto
product_bst.change_quantity(103, 10)

# Obtenção de produtos com quantidade mínima
products = product_bst.get_products_with_min_quantity(4)
print(products) # Saída esperada: Lista de nós com quantidade maior que 4
```

### Utilização de `Product_node`

```python
from Classes.Product_node import Product_node

node = Product_node(13)
print(node)       # Saída esperada: "13"

# Linkando nós
node.left = Product_node(10, 4)
node.right = Product_node(15)

p_id: 101 quantity: 5
print(node.left)  # Saída esperada: "p_id: 10 quantity: 4" 
print(node.right) # Saída esperada: "p_id: 15 quantity: 1"
```
---
### **Resumo do README**
Este README é organizado para facilitar a compreensão do propósito do projeto, a estrutura do código, e os passos necessários para configuração e execução. Também inclui exemplos claros para ajudar novos usuários e desenvolvedores a começarem rapidamente.

## **Colaboradores**
Trabalho de Estrutura de Dados com os devidos créditos para:
- [Arthur Vinicius Carneiro Nunes](https://github.com/ApenasUmSonhador) - Questões 1 e 3
- [Caio Passos De Lima Albuquerque](https://github.com/CaioPassos3) - Questões 7 e 9
- Gleidistony Mendes Martins - Questão 5
- [Mateus Santos Araújo](https://github.com/Matheus-Santos-Araujo) - Professor da disciplina

