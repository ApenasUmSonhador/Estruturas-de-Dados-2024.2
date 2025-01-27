from setup_paths import setup
setup()  # Configura o caminho para acessar as classes
from Product_node import Product_node
import time
def test_product_node():
    print("--------------------")
    print("Test Product Node Performance")

    def create_nodes(n):
        nodes = []
        for i in range(n):
            nodes.append(Product_node(i))
        return nodes

    def link_nodes(nodes):
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i + 1].left = nodes[i]

    sizes = [100, 1000, 10000, 100000, 1000000]

    for size in sizes:
        print(f"\nTest with {size} nodes")

        print("Creating nodes")
        time.start = time.time()
        nodes = create_nodes(size)
        time.end = time.time()
        print("Time:", time.end - time.start)

        print("Linking nodes")
        time.start = time.time()
        link_nodes(nodes)
        time.end = time.time()
        print("Time:", time.end - time.start)

        print("Removing nodes")
        time.start = time.time()
        for node in nodes:
            node.left = None
            node.right = None
        time.end = time.time()
        print("Time:", time.end - time.start)

    print("--------------------")

if __name__ == "__main__":
    test_node_performance()