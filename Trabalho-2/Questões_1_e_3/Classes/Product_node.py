class Product_node:
    # Construtor da classe O(1)
    def __init__(self, id, quantity = 1):
        self.id = id
        self.quantity = quantity
        self.right = None
        self.left = None

    # Método para representação em string O(1)
    def __str__(self):
        return str(self.data)