from Stack import Stack

class Calculator:
    def __init__(self, is_test = False, expression = None,is_postfix = False):  # O(1)
        # Inicializa valores padrão para as variáveis
        self.values = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10
        }
        # Definindo as operações
        self.OP = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        # Se não for um teste, solicita os valores e a expressão do usuário
        if not is_test:
            # Solicitar valores para as variáveis
            for var in self.values.keys():
                self.values[var] = float(input(f"Enter the value for {var}: "))
            
            # Solicitar a expressão do usuário com base no formato escolhido
            self.is_postfix = input("Is the expression in postfix? (y/n): ").strip().lower() == 'y'
            expression_type = "postfix" if self.is_postfix else "infix"
            self.expression = input(f"Enter the {expression_type} expression: ").strip()

            # Validando a expressão
            if not isinstance(self.expression, str):
                raise ValueError("Invalid expression")
        
        # Se for um teste, utiliza os valores e a expressão passados como parâmetro
        else:
            self.expression = expression
            self.is_postfix = is_postfix

        # Limpeza de espaços em branco e validação de variáveis
        self.expression = ''.join([char for char in self.expression if char != ' '])
        for char in self.expression:
            if char.isalpha() and char not in self.values:
                raise ValueError(f"Invalid variable in expression: {char}")

    def precedence(self, op):  # O(1)
        # Define a precedência dos operadores
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        if op == '^':
            return 3
        return 0

    def infix_to_postfix(self):  # O(n)
        # Converte a expressão infixa para pós-fixa
        stack = Stack()
        result = []
        for char in self.expression:
            if char.isalpha():
                result.append(char)
            elif char == '(':
                stack.push(char)
            elif char == ')':
                while not stack.is_empty() and stack.get_top() != '(':
                    result.append(stack.pop())
                stack.pop()  # Remove o '(' da pilha
            else:
                while not stack.is_empty() and self.precedence(char) <= self.precedence(stack.get_top()):
                    result.append(stack.pop())
                stack.push(char)
        # Desempilha os operadores restantes
        while not stack.is_empty():
            result.append(stack.pop())
        return ''.join(result)

    def calculate(self):  # O(n)
        # Avalia uma expressão pós-fixa
        stack = Stack()
        # Converte infixa para pós-fixa se necessário
        if not self.is_postfix:
            self.expression = self.infix_to_postfix()

        for char in self.expression:
            if char.isalpha():
                stack.push(self.values[char])
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                stack.push(self.OP[char](val1, val2))
        return stack.pop()