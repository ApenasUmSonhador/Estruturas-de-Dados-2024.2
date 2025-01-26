import sys
from setup_paths import setup
setup()  # Configura o caminho para acessar as classes
import time
from Product_bst import Product_bst
from Product_node import Product_node

def test_bst_performance():
    print("--------------------")
    print("Test Product BST Performance")

    def create_bst(n):
        bst = Product_bst()
        for i in range(n):
            bst.insert(i)
        return bst

    sizes = [10, 100, 1000] 
    # Valores maiores causam estouro de máximo de recursão
    # O valor 1000 já é suficiente para mostrar a diferença de desempenho
    # Fora que lidar com python e recursão não é uma boa ideia
    # Ele não é otimizado para isso

    for size in sizes:
        print(f"\nTest with {size} nodes")

        print("Creating BST")
        time_start = time.time()
        bst = create_bst(size)
        time_end = time.time()
        print("Time:", time_end - time_start)

        print("Searching nodes")
        time_start = time.time()
        for i in range(size):
            bst.search(i)
        time_end = time.time()
        print("Time:", time_end - time_start)

        print("Removing nodes")
        time_start = time.time()
        for i in range(size):
            bst.remove(i)
        time_end = time.time()
        print("Time:", time_end - time_start)

        print(f"Completed test with {size} nodes")

    print("--------------------")

if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    test_bst_performance()