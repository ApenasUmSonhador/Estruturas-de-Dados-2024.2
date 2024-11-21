from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Converter import Converter
def test_converter():
    is_correct = True
    print("--------------------")
    print("Test Converter")
    print("\nBinary")

    print("Test 1")
    c1 = Converter(13)
    print("Result:", c1.to_binary())
    print("Expected: 1101")
    is_correct = is_correct and c1.to_binary() == "1101"

    print("Test 2")
    c2 = Converter(255)
    print("Result:", c2.to_binary())
    print("Expected: 11111111")
    is_correct = is_correct and c2.to_binary() == "11111111"

    print("Test 3")
    c3 = Converter(0)
    print("Result:", c3.to_binary())
    print("Expected: 0")
    is_correct = is_correct and c3.to_binary() == "0"

    print("\nOctal")
    print("Test 1")
    c1 = Converter(13)
    print("Result:", c1.to_octal())
    print("Expected: 15")
    is_correct = is_correct and c1.to_octal() == "15"

    print("Test 2")
    c2 = Converter(255)
    print("Result:", c2.to_octal())
    print("Expected: 377")
    is_correct = is_correct and c2.to_octal() == "377"

    print("Test 3")
    c3 = Converter(0)
    print("Result:", c3.to_octal())
    print("Expected: 0")
    is_correct = is_correct and c3.to_octal() == "0"

    print("\nHexadecimal")
    print("Test 1")
    c1 = Converter(13)
    print("Result:", c1.to_hexadecimal())
    print("Expected: D")
    is_correct = is_correct and c1.to_hexadecimal() == "D"

    print("Test 2")
    c2 = Converter(255)
    print("Result:", c2.to_hexadecimal())
    print("Expected: FF")
    is_correct = is_correct and c2.to_hexadecimal() == "FF"

    print("Test 3")
    c3 = Converter(0)
    print("Result:", c3.to_hexadecimal())
    print("Expected: 0")
    is_correct = is_correct and c3.to_hexadecimal() == "0"

    return is_correct

test_converter()