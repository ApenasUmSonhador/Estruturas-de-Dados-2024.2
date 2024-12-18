from setup_init_paths import setup
# Configura o caminho para acessar os testes
setup()

# Importa e executa os testes
from test_stack import test_stack
from test_converter import test_converter
from test_calculator import test_calculator

if (test_stack() and test_converter() and test_calculator()):
    print("All tests passed in all Classes")
else:
    print("Some tests did'nt passed in all Classes")