class Product_node:
    # Construtor da classe O(1)
    def __init__(self, p_id, quantity = 1):
        self.p_id = p_id
        self.quantity = quantity
        self.right = None
        self.left = None

    # Método para representação em string O(1)
    def __str__(self):
        return f"p_id: {self.p_id}, quantity: {self.quantity}"