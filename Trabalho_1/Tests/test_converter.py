from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Converter import Converter
def test_converter():
    converter = Converter(13)
    print(converter.to_binary())
    print(converter.to_octal())
    print(converter.to_hexadecimal())