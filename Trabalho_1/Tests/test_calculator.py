from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Calculator import Calculator
def test_calculator():
    is_correct = True
    print("--------------------")
    print("Test Calculator")

    print("\nInfix notation")
    print("Test 1")
    c1 = Calculator(True, "A+B*C-D/E^F+G-H*I+J", False)
    result = c1.calculate()
    print("Result:", result)
    expected = 1 + 2 * 3 - 4 / 5 ** 6 + 7 - 8 * 9 + 10
    print("Expected: ", expected)
    is_correct = is_correct and result == expected

    print("Test 2")
    c2 = Calculator(True, "C+D*B/(A-E)^B", False)
    result = c2.calculate()
    print("Result:", result)
    expected = 3 + 4 * 2 / (1-5) ** 2
    print("Expected: ", expected)
    is_correct = is_correct and result == expected

    print("Test 3")
    c3 = Calculator(True, "J+((C*E)+(H/D))", False)
    result = c3.calculate()
    print("Result:", result)
    expected = 10 + ((3 * 5) +(8 / 4))
    print("Expected: ", expected)
    is_correct = is_correct and result == expected
    
    print("\nPostfix notation")
    print("Test 1")
    c4 = Calculator(True, "C D B * A E - B ^ / +", True)
    result = c4.calculate()
    print("Result:", result)
    expected = 3 + 4 * 2 / (1-5) ** 2
    print("Expected: ", expected)
    is_correct = is_correct and result == expected

    print("Test 2")
    c5 = Calculator(True, "J C E * H D / + +", True)
    result = c5.calculate()
    print("Result:", result)
    expected = 10 + ((3 * 5) +(8 / 4))
    print("Expected: ", expected)
    is_correct = is_correct and result == expected

    print("Test 3")
    c6 = Calculator(True, "D E F ^ / G - H I * + J +", True)
    result = c6.calculate()
    print("Result:", result)
    expected = (4 / (5 ** 6) - 7) + 8 * 9 + 10
    print("Expected: ", expected)
    is_correct = is_correct and result == expected

    return is_correct

test_calculator()