from setup_init_paths import setup
# Configura o caminho para acessar os testes
setup()

# Importa e executa os testes
from test_node import test_node
from test_bst import test_bst
from test_product_node import test_product_node
from test_procuct_bst import test_procuct_bst

if (test_node() and test_bst() and test_product_node() and test_procuct_bst()):
    print("All tests passed in all Classes")
else:
    print("Some tests did'nt passed in all Classes")