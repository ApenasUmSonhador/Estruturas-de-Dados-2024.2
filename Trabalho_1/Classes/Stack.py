class Stack:
    def __init__(self, capacity = 64):  # O(n)
        # Cria uma pilha com capacidade definida, padrão 64
        self.capacity = capacity
        # Inicializa o índice do topo da pilha
        self.top_index = -1
        # Inicializa a lista de elementos da pilha
        self.elements = [None] * capacity
    
    def is_empty(self):  # O(1)
        # Se index do topo for -1, a pilha está vazia
        return self.top_index == -1

    def is_full(self):  # O(1)
        # Se index do topo for igual à capacidade - 1, a pilha está cheia
        return self.top_index == self.capacity - 1

    def push(self, element):  # O(1)
        # Se a pilha estiver cheia, não é possível adicionar elementos
        if self.is_full():
            raise Exception("Stack is full")
        # Incrementa o índice do topo e adiciona o elemento no topo
        self.top_index += 1
        self.elements[self.top_index] = element
    
    def pop(self):  # O(1)
        # Se a pilha estiver vazia, não é possível remover elementos
        if self.is_empty():
            raise Exception("Stack is empty")
        # Decrementa o índice do topo e retorna o elemento do topo
        self.top_index -= 1
        return self.elements[self.top_index + 1]
    
    def get_top(self):  # O(1)
        # Se a pilha estiver vazia, não há topo para retornar
        if self.is_empty():
            raise Exception("Stack is empty")
        # Retorna o elemento do topo
        return self.elements[self.top_index]

    def print_stack(self):  # O(n)
        # Leio os elementos da pilha do topo para a base e imprimo
        for i in range(self.top_index, -1, -1):
            print(self.elements[i])
    
    def print_reverse(self):  # O(n)
        # Leio os elementos da pilha da base para o topo e imprimo
        for i in range(0, self.top_index + 1):
            print(self.elements[i])

    def free(self):  # O(1)
        # em Python, não precisamos liberar memória
        # porque os elementos serão coletados pelo garbage collector
        # então, este método é inútil, mas vou implementá-lo de qualquer forma
        # para manter a mesma estrutura do código em C
        # e para manter a mesma assinatura do método
        # ...mas ele não fará nada
        pass
    
    def delete(self, element):  # O(n)
        # Crio uma pilha temporária para armazenar os elementos removidos
        temp_stack = Stack(self.top_index + 1)
        # Variável para indicar se o elemento foi encontrado
        found = False

        # Vou removendo elementos da pilha original e adicionando na pilha temporária
        while not self.is_empty():
            top_element = self.pop()
            # Se o elemento do topo for igual ao elemento a ser removido, eu paro de remover
            if top_element == element:
                found = True
                break
            # Senão, eu adiciono o elemento removido na pilha temporária
            temp_stack.push(top_element)

        # Vou removendo elementos da pilha temporária e adicionando de volta na pilha original
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        # temp_stack.free() # Não é necessário liberar a pilha temporária, por motivos de... python

        if not found:
            raise Exception("Element not found in stack")

    # Existem 2 formas de resolver este problema:
    # 1. Utilizando pilha (creio que é como queria que fosse feito)
    def is_palindrome(self, string):  # O(n)
        # Adiciono todos os caracteres da string na pilha
        for char in string:
            self.push(char)
        
        # Comparo os caracteres da string com os elementos da pilha
        for char in string:
            if char != self.pop():
                return False
        # Ou seja, basicamente eu comparo a string original com a string invertida
        return True

    # 2. Utilizando a estraégia de dois ponteiros (é o que acho mais elegante e eficiente)
    # ...mas como você pediu para ser feito com pilha, fiz com pilha acima
    # Leetcode: https://leetcode.com/problems/valid-palindrome/
    def is_palindrome_pointers(self, string):  # O(n)

        left, right = 0, len(string) - 1
        # Enquanto os ponteiros não se cruzarem
        while left < right:
            # Se os caracteres não forem iguais, a string não é um palíndromo
            if string[left] != string[right]:
                return False
            # Avança o ponteiro da esquerda e retrocede o ponteiro da direita
            left += 1
            right -= 1
        # Se os ponteiros se cruzarem, a string é um palíndromo
        return True

    def odd_and_evens(self, number_list):  # O(n)
        # Adiciono todos os números na pilha
        for number in number_list:
            self.push(number)
        # Crio duas pilhas para armazenar os números pares e ímpares
        odd_stack = Stack(self.capacity)
        even_stack = Stack(self.capacity)

        # Vou removendo os elementos da pilha original e adicionando nas pilhas de pares e ímpares
        for _ in range(self.top_index + 1, self.top_index - len(number_list) + 1, -1):
            top_element = self.pop()
            if top_element % 2 == 0:
                even_stack.push(top_element)
            else:
                odd_stack.push(top_element)
        # Ao final, terei pilhas com os números pares e ímpares na mesma ordem que estavam em number_list
        return odd_stack, even_stack