class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top_index = -1
        self.elements = [None] * capacity
    
    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.capacity - 1

    def push(self, element):
        if self.is_full():
            raise Exception("Stack is full")
        self.top_index += 1
        self.elements[self.top_index] = element
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        self.top_index -= 1
        return self.elements[self.top_index + 1]
    
    def get_top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.elements[self.top_index]

    def print_stack(self):
        for i in range(self.top_index, -1, -1):
            print(self.elements[i])
    
    def print_reverse(self):
        for i in range(0, self.top_index + 1):
            print(self.elements[i])

    def free(self):
        # in python, we don't need to free memory
        # because the elements will be garbage collected
        # soo, this method is useless, but I'll implement it anyway
        # to keep the same structure as the C code
        # and to keep the same method signature
        # ... but it won't do anything
        pass
    
    def delete(self, element):
        temp_stack = Stack(self.top_index + 1)
        found = False

        while not self.is_empty():
            top_element = self.pop()
            if top_element == element:
                found = True
                break
            temp_stack.push(top_element)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        # self.free()
        # in python, we don't need to free memory

        if not found:
            raise Exception("Element not found in stack")

    def is_palindrome(self, string):
        for char in string:
            self.push(char)
        
        for char in string:
            if char != self.pop():
                return False

        return True

    def odd_and_evens(self, number_list):
        for number in number_list:
            self.push(number)
        odd_stack = Stack(self.capacity)
        even_stack = Stack(self.capacity)
        for _ in range(self.top_index + 1, self.top_index - len(number_list) + 1, -1):
            top_element = self.pop()
            if top_element % 2 == 0:
                even_stack.push(top_element)
            else:
                odd_stack.push(top_element)
        return odd_stack, even_stack