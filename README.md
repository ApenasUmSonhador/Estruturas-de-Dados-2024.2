# **Estruturas de Dados 2024.2**

Este projeto é uma implementação de algoritmos e estruturas de dados desenvolvidos no contexto do curso **Estrutura de Dados**, ministrado pelo professor **Me. Matheus Araújo** durante o **bacharelado em Ciência da Computação** pela **Universidade Federal do Ceará (UFC)** no semestre **2024.2**. Ele é organizado em módulos bem definidos, com testes automatizados para garantir a correção e a confiabilidade do código.

---

## **Estrutura do Projeto**

A estrutura do projeto segue a seguinte organização:
```yaml
ED-2024.2/
├── Trabalho_1/
│   ├── __init__.py                # Arquivo principal que executa os testes
│   ├── setup_init_paths.py        # Arquivo que configura paths para __init__.py
│   ├── Tests/                     # Pasta com testes automatizados 
│   │   ├── setup_paths.py         # Arquivo que configura paths para os testes
│   │   ├── test_calculator.py          # Testes relacionados à calculadora
│   │   ├── test_stack.py          # Testes relacionados à estrutura de pilha
│   │   ├── test_converter.py      # Testes relacionados ao módulo de conversão
│   └── Classes/                   # Pasta com as implementações principais
│       ├── Calculator.py          # Implementação da calculadora
│       ├── Converter.py           # Implementação do módulo de conversão
│       ├── Stack.py               # Implementação da estrutura de pilha

```

---

## **Funcionalidades**

- **Classes/Calculator.py**  
  Implementa funções capazes de solucionar expressões de 10 variáveis em notação infixa e pós-fixa (RPN)

- **Classes/Converter.py**  
  Implementa funções para conversão de inteiros de base 10 em diferentes bases.  

- **Classes/Stack.py**  
  Implementa uma estrutura de pilha com operações básicas como `push`, `pop` e verificação de vazio.

- **Tests/test_calculator.py**  
  Contém testes automatizados para validar o comportamento correto da classe `Calculator`.

- **Tests/test_stack.py**  
  Contém testes automatizados para validar o comportamento correto da classe `Stack`.

- **Tests/test_converter.py**  
  Contém testes automatizados para validar o comportamento do módulo `Converter`.  

---

## **Configuração**

1. Certifique-se de que o Python 3.8+ está instalado no sistema.  

2. Clone o repositório:

```bash
   git clone <url-do-repositorio>
   cd ED-2024.2/Trabalho_1
```

---

## **Como executar**
### Rodar os testes
Para executar os testes automatizados diretamente, rode o seguinte comando na pasta Trabalho_1:

```bash
python __init__.py
```
Isso importará e executará os módulos de teste, garantindo que as implementações estejam funcionando corretamente.

---

## **Exemplo de Uso**
### Conversão com `Converter`

```python
from Classes.Converter import Converter

converter = Converter(13)
resultado = converter.to_hexadecimal 
print(resultado)  # Saída esperada: "D"
```

### Operações com `Stack`
```python
from Classes.Stack import Stack

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # Saída: 20
print(stack.is_empty())  # Saída: False
```

### Operações com `Calculator`
```python
from Classes.Calculator import Calculator

calculator = Calculator() # Entrada: Valor das variáveis, expressão e se é da forma pós-fixa
result = caculator.calculate() 
print(result)  # Saída: Cálculo baseado no input
```

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

### **Resumo do README**
Este README é organizado para facilitar a compreensão do propósito do projeto, a estrutura do código, e os passos necessários para configuração e execução. Também inclui exemplos claros para ajudar novos usuários e desenvolvedores a começarem rapidamente.
