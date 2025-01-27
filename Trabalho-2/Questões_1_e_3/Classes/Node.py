class Node:
    # Construtor da classe O(1)
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    # Método para representação em string O(1)
    def __str__(self):
        return str(self.value)