from Stack import Stack
class Converter:
    def __init__(self, value):  # O(1)
        self.value = value
    
    def to_binary(self):  # O(log n)
        return self.convert(2)
    
    def to_octal(self):  # O(log n)
        return self.convert(8)
    
    def to_hexadecimal(self):  # O(log n)
        return self.convert(16)

    def convert(self, base):  # O(log n)
        # Cria uma pilha com capacidade de 64 elementos
        stack = Stack(64)
        result = ""
        value = self.value

        # Converte o valor para a base desejada
        while value > 0:
            # Empilha o resto da divisão do valor pela base
            stack.push(value % base)
            # Atualiza o valor para o quociente da divisão
            value = value // base
        
        # Desempilha todos os elementos e constrói a string do resultado
        while not stack.is_empty():
            top_element = stack.pop()
            if top_element < 10:
                # Se o elemento for menor que 10, converte diretamente para string
                result += str(top_element)
            else:
                # Se o elemento for 10 ou maior, converte para o caractere correspondente (A, B, C, etc.)
                # ASCII de A é 65, de B é 66, etc.
                # então adicionamos 55 ao valor do elemento para obter o caractere correto
                result += chr(55 + top_element)
        
        # Retorna o resultado final da conversão
        if result == "":
            result = "0"
        return result