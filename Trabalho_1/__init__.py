from setup_init_paths import setup
# Configura o caminho para acessar os testes
setup()

# Importa e executa os testes
from test_stack import test_stack
from test_converter import test_converter

test_stack()
test_converter()