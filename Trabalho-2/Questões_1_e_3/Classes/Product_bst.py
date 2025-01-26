class Product_bst:
    # Construtor da classe 
    def __init__(self, node=None): # O(1)
        self.root = node
    
    # Método para inserir um valor na árvore
    def insert(self, value): # O(log n)
        if self.root is None:
            self.root = Product_node(value)
        else:
            self._insert_recursive(self.root, value)
        
    # Método auxiliar para inserir um valor na árvore
    def _insert_recursive(self, current_node, value): # O(log n)
        if value.id < current_node.id:
            if current_node.left is None:
                current_node.left = Product_node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value.id > current_node.id:
            if current_node.right is None:
                current_node.right = Product_node(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            current_node.quantity += value.quantity
        
    # Método para remover um valor da árvore
    def remove(self, value): # O(log n)
        self._remove_recursive(self.root)

    # Método auxiliar para remover um valor da árvore
    def _remove_recursive(self, current_node):
        if current_node is None:
            return current_node
        if id < current_node.id:
            current_node.left = self._remove_recursive(current_node.left)
        elif id > current_node.id:
            current_node.right = self._remove_recursive(current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            current_node.id = self._min_value(current_node.right)
            current_node.right = self._remove_recursive(current_node.right)
        return current_node

    def search(self, id):
        return self._search_recursive(self.root, id)

    def _search_recursive(self, current_node, id):
        if current_node is None:
            return None
        if id < current_node.id:
            return self._search_recursive(current_node.left, id)
        elif id > current_node.id:
            return self._search_recursive(current_node.right, id)
        else:
            return current_node
    
    def change_quantity(self, id, quantity):
        node = self.search(id)
        if node is not None:
            node.quantity = quantity
    
    def _min_id(self, current_node):
        if current_node.left is None:
            return current_node
        return self._min_id(current_node.left)
    
    def _max_id(self, current_node):
        if current_node.right is None:
            return current_node
        return self._max_id(current_node.right)
    
    def get_products_with_min_quantity(self, min_quantity):
        result = []
        self._get_products_with_min_quantity_recursive(self.root, min_quantity, result)
        return result

    def _get_products_with_min_quantity_recursive(self, current_node, min_quantity, result):
        if current_node is not None:
            if current_node.quantity > min_quantity:
                result.append(current_node)
            self._get_products_with_min_quantity_recursive(current_node.left, min_quantity, result)
            self._get_products_with_min_quantity_recursive(current_node.right, min_quantity, result)