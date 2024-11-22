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
    result = c1.to_binary()
    print("Result:", result)
    print("Expected: 1101")
    is_correct = is_correct and result == "1101"

    print("Test 2")
    c2 = Converter(255)
    result = c2.to_binary()
    print("Result:", result)
    print("Expected: 11111111")
    is_correct = is_correct and result == "11111111"

    print("Test 3")
    c3 = Converter(0)
    result = c3.to_binary()
    print("Result:", result)
    print("Expected: 0")
    is_correct = is_correct and result == "0"

    print("\nOctal")
    print("Test 1")
    c1 = Converter(13)
    result = c1.to_octal()
    print("Result:", result)
    print("Expected: 15")
    is_correct = is_correct and result == "15"

    print("Test 2")
    c2 = Converter(255)
    result = c2.to_octal()
    print("Result:", result)
    print("Expected: 377")
    is_correct = is_correct and result == "377"

    print("Test 3")
    c3 = Converter(0)
    result = c3.to_octal()
    print("Result:", result)
    print("Expected: 0")
    is_correct = is_correct and result == "0"

    print("\nHexadecimal")
    print("Test 1")
    c1 = Converter(13)
    result = c1.to_hexadecimal()
    print("Result:", result)
    print("Expected: D")
    is_correct = is_correct and result == "D"

    print("Test 2")
    c2 = Converter(255)
    result = c2.to_hexadecimal()
    print("Result:", result)
    print("Expected: FF")
    is_correct = is_correct and result == "FF"

    print("Test 3")
    c3 = Converter(0)
    result = c3.to_hexadecimal()
    print("Result:", result)
    print("Expected: 0")
    is_correct = is_correct and result == "0"

    print("\nAny base")
    print("Test 1")
    c1 = Converter(13)
    result = c1.convert(10)
    print("Result:", result)
    print("Expected: 13")
    is_correct = is_correct and result == "13"

    print("Test 2")
    c2 = Converter(255)
    result = c2.convert(29)
    print("Result:", result)
    print("Expected: 8N")
    is_correct = is_correct and result == "8N"

    print("Test 3")
    c3 = Converter(0)
    result = c3.convert(7)
    print("Result:", result)
    print("Expected: 0")
    is_correct = is_correct and result == "0"

    print()
    if is_correct:
        print("All tests passed")
    else:
        print("Some tests failed")
    print("--------------------")
    return is_correct