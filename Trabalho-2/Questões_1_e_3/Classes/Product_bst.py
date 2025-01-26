from Product_node import Product_node
class Product_bst:
    # Construtor da classe 
    def __init__(self, node=None): # O(1)
        self.root = node
    
    # Método para inserir um valor na árvore
    def insert(self, p_id, quantity=1): # O(log n)
        if self.root is None:
            self.root = Product_node(p_id, quantity)
        else:
            self._insert_recursive(self.root, p_id, quantity)
        
    # Método auxiliar para inserir um valor na árvore
    def _insert_recursive(self, current_node, p_id, quantity): # O(log n)
        if p_id < current_node.p_id:
            if current_node.left is None:
                current_node.left = Product_node(p_id, quantity)
            else:
                self._insert_recursive(current_node.left, p_id, quantity)
        elif p_id > current_node.p_id:
            if current_node.right is None:
                current_node.right = Product_node(p_id, quantity)
            else:
                self._insert_recursive(current_node.right, p_id, quantity)
        else:
            current_node.quantity += quantity
        
    # Método para remover um valor da árvore
    def remove(self, p_id): # O(log n)
        self.root = self._remove_recursive(self.root, p_id)

    # Método auxiliar para remover um valor da árvore
    def _remove_recursive(self, current_node, p_id):
        if current_node is None:
            return current_node
        if p_id < current_node.p_id:
            current_node.left = self._remove_recursive(current_node.left)
        elif p_id > current_node.p_id:
            current_node.right = self._remove_recursive(current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            min_larger_node = self._min_p_id(current_node.right)
            current_node.p_id = min_larger_node.p_id
            current_node.quantity = min_larger_node.quantity
            current_node.right = self._remove_recursive(current_node.right, min_larger_node.p_id)
        return current_node

    def search(self, p_id):
        return self._search_recursive(self.root, p_id)

    def _search_recursive(self, current_node, p_id):
        if current_node is None:
            return None
        if p_id < current_node.p_id:
            return self._search_recursive(current_node.left, p_id)
        elif p_id > current_node.p_id:
            return self._search_recursive(current_node.right, p_id)
        else:
            return current_node
    
    def change_quantity(self, p_id, quantity):
        node = self.search(p_id)
        if node is not None:
            node.quantity = quantity
    
    def _min_p_id(self, current_node):
        if current_node.left is None:
            return current_node
        return self._min_p_id(current_node.left)
    
    def _max_p_id(self, current_node):
        if current_node.right is None:
            return current_node
        return self._max_p_id(current_node.right)
    
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