from Stack import Stack
class Converter:
    def __init__(self, value):
        self.value = value
    
    def to_binary(self):
        return self.convert(2)
    
    def to_octal(self):
        return self.convert(8)
    
    def to_hexadecimal(self):
        return self.convert(16)

    def convert(self, base):
        stack = Stack(64)
        result = ""
        value = self.value

        while value > 0:
            stack.push(value % base)
            value = value // base
        while not stack.is_empty():
            top_element = stack.pop()
            if top_element < 10:
                result += str(top_element)
            else:
                result += chr(55 + top_element)
        return result