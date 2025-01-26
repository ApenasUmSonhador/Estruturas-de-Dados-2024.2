from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

import time
import random
from Bst import Bst
from Node import Node

def generate_values(n):
    return [random.randint(1, 1000000) for _ in range(n)]

def test_bst_performance():
    sizes = [100, 1000, 10000, 100000, 1000000]
    for size in sizes:
        values = generate_values(size)
        bst = Bst()

        print(f"\nTesting with {size} values")

        # Test insert
        start_time = time.time()
        for value in values:
            bst.insert(value)
        end_time = time.time()
        print(f"Insert time for {size} values: {end_time - start_time} seconds")

        # Test remove
        start_time = time.time()
        for value in values:
            bst.remove(value)
        end_time = time.time()
        print(f"Remove time for {size} values: {end_time - start_time} seconds")

if __name__ == "__main__":
    test_bst_performance()