from Node import Node

class Bst:
    # Construtor da classe
    def __init__(self, node=None): # O(1)
        self.root = node

    # Método para inserir um valor na árvore
    def insert(self, value): # O(log n)
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Método auxiliar para inserir um valor na árvore
    def _insert_recursive(self, current_node, value): # O(log n)
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    # Método para remover um valor da árvore
    def remove(self, value): # O(log n)
        self._remove_recursive(self.root, value)

    # Método auxiliar para remover um valor da árvore
    def _remove_recursive(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.value:
            current_node.left = self._remove_recursive(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self._remove_recursive(current_node.right, value)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left
            current_node.value = self._min_value(current_node.right)
            current_node.right = self._remove_recursive(current_node.right, current_node.value)
        return current_node

    # Método para encontrar a altura da árvore
    def height(self): # O(n)
        return self._height_recursive(self.root)
    
    # Método auxiliar para encontrar a altura da árvore
    def _height_recursive(self, current_node): # O(n)
        if current_node is None:
            return 0
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return max(left_height, right_height) + 1

    # Método para buscar um valor na árvore
    def search(self, value): # O(log n)
        return self._search_recursive(self.root, value)

    # Método auxiliar para buscar um valor na árvore
    def _search_recursive(self, current_node, value): # O(log n)
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    # Método para achar o valor máximo da árvore
    def get_max_value(self): # O(log n)
        return self._max_value(self.root)

    # Método auxiliar para achar o valor máximo da árvore
    def _max_value(self, current_node): # O(log n)
        if current_node.right is None:
            return current_node.value
        return self._max_value(current_node.right)

    # Método para achar o valor mínimo da árvore
    def get_min_value(self): # O(log n)
        return self._min_value(self.root)

    # Método auxiliar para achar o valor mínimo da árvore
    def _min_value(self, current_node): # O(log n)
        if current_node.left is None:
            return current_node.value
        return self._min_value(current_node.left)
    
    # Método para encontrar o sucessor ao valor passado
    def next_value(self, value): # O(log n)
        return self._next_recursive(self.root, value)
    
    # Método auxiliar para encontrar o sucessor ao valor passado
    def _next_recursive(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value <= value:
            return self._next_recursive(current_node.right, value)
        left = self._next_recursive(current_node.left, value)
        return left if left is not None else current_node.value

    # Método para encontrar o antecessor ao valor passado
    def previous_value(self, value): # O(log n)
        return self._previous_recursive(self.root, value)
    
    # Método auxiliar para encontrar o antecessor ao valor passado
    def _previous_recursive(self, current_node, value): # O(log n)
        if current_node is None:
            return None
        if current_node.value >= value:
            return self._previous_recursive(current_node.left, value)
        right = self._previous_recursive(current_node.right, value)
        return right if right is not None else current_node.value
    
    # Método para percorrer a árvore em pré-ordem
    def pre_order(self): # O(n)
        return self._pre_order_recursive(self.root)
    
    # Método auxiliar para percorrer a árvore em pré-ordem
    def _pre_order_recursive(self, current_node): # O(n)
        if current_node is None:
            return []
        return [current_node.value] + self._pre_order_recursive(current_node.left) + self._pre_order_recursive(current_node.right)

    # Método para percorrer a árvore em ordem
    def in_order(self): # O(n)
        return self._in_order_recursive(self.root)
    
    # Método auxiliar para percorrer a árvore em ordem
    def _in_order_recursive(self, current_node): # O(n)
        if current_node is None:
            return []
        return self._in_order_recursive(current_node.left) + [current_node.value] + self._in_order_recursive(current_node.right)

    # Método para percorrer a árvore em pós-ordem
    def post_order(self): # O(n)
        return self._post_order_recursive(self.root)
    
    # Método auxiliar para percorrer a árvore em pós-ordem
    def _post_order_recursive(self, current_node): # O(n)
        if current_node is None:
            return []
        return self._post_order_recursive(current_node.left) + self._post_order_recursive(current_node.right) + [current_node.value]

    # Método para verificar se a árvore está balanceada
    def is_balanced(self): # O(n)
        return self._is_balanced_recursive(self.root)

    # Método auxiliar para verificar se a árvore está balanceada
    def _is_balanced_recursive(self, current_node): # O(n)
        if current_node is None:
            return True
        left_height = self._height_recursive(current_node.left)
        right_height = self._height_recursive(current_node.right)
        return abs(left_height - right_height) <= 1 and self._is_balanced_recursive(current_node.left) and self._is_balanced_recursive(current_node.right)

    def all_values_in_range(self, min_value, max_value): # O(n)
        return self._all_values_in_range_recursive(self.root, min_value, max_value)
    
    def _all_values_in_range_recursive(self, current_node, min_value, max_value): # O(n)
        if current_node is None:
            return []
        if current_node.value < min_value:
            return self._all_values_in_range_recursive(current_node.right, min_value, max_value)
        if current_node.value > max_value:
            return self._all_values_in_range_recursive(current_node.left, min_value, max_value)
        return self._all_values_in_range_recursive(current_node.left, min_value, max_value) + [current_node.value] + self._all_values_in_range_recursive(current_node.right, min_value, max_value)

    # Método para representação em string
    def __str__(self): # O(n)
        return str(self.in_order())
