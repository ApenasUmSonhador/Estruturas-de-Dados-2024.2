from setup_init_paths import setup
# Configura o caminho para acessar os testes
setup()

import sys
sys.setrecursionlimit(10**5)

# Importa e executa os testes
from test_node import test_node
from test_bst import test_bst
from test_product_node import test_product_node
from test_product_bst import test_product_bst

try:
    test_node()
    test_bst()
    test_product_node()
    test_product_bst()
    print("All tests passed in all Classes")
except Exception as e:
    print(e.with_traceback())
    print("An error occurred during the tests")
    print(e)
