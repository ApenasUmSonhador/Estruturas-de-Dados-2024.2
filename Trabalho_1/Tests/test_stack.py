from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Stack import Stack

def test_stack():
    is_correct = True
    print("--------------------")
    print("Test Stack")

    print("\nPush and Pop")
    print("Test 1")
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    result = s1.pop()
    print("Result:", result)
    print("Expected: 3")
    is_correct = is_correct and result == 3

    print("Test 2")
    result = s1.pop()
    print("Result:", result)
    print("Expected: 2")
    is_correct = is_correct and result == 2

    print("Test 3")
    result = s1.pop()
    print("Result:", result)
    print("Expected: 1")
    is_correct = is_correct and result == 1
    s1.free() # Sonha que a memória foi liberada

    print("\nGet Top")
    print("Test 1")
    s2 = Stack()
    s2.push(10)
    result = s2.get_top()
    print("Result:", result)
    print("Expected: 10")
    is_correct = is_correct and result == 10

    print("Test 2")
    s2.push(20)
    result = s2.get_top()
    print("Result:", result)
    print("Expected: 20")
    is_correct = is_correct and result == 20
    s2.free() # Sonha que a memória foi liberada

    print("\nIs Empty")
    print("Test 1")
    s3 = Stack()
    result = s3.is_empty()
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True

    print("Test 2")
    s3.push(5)
    result = s3.is_empty()
    print("Result:", result)
    print("Expected: False")
    is_correct = is_correct and result is False

    print("\nIs full")
    print("Test 1")
    s3 = Stack(1)
    result = s3.is_full()
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is False

    print("Test 2")
    s3.push(5)
    result = s3.is_full()
    print("Result:", result)
    print("Expected: False")
    is_correct = is_correct and result is True
    s3.free() # Sonha que a memória foi liberada

    print("\nDelete")
    print("Test 1")
    s4 = Stack()
    s4.push(1)
    s4.push(2)
    s4.push(3)
    s4.delete(2)
    result = s4.get_top()
    print("Result:", result)
    print("Expected: 3")
    is_correct = is_correct and result == 3

    print("Test 2")
    s4.delete(3)
    result = s4.get_top()
    print("Result:", result)
    print("Expected: 1")
    is_correct = is_correct and result == 1

    print("Test 3")
    s4.delete(1)
    result = s4.is_empty()
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True
    s4.free() # Sonha que a memória foi liberada

    print("\nIs Palindrome")
    print("Test 1")
    s5 = Stack()
    result = s5.is_palindrome("ana")
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True

    print("Test 2")
    result = s5.is_palindrome("arara")
    reuslt = s5.is_palindrome("arara")
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True

    print("Test 3")
    result = s5.is_palindrome("palindrome")
    print("Result:", result)
    print("Expected: False")
    is_correct = is_correct and result is False
    s5.free() # Sonha que a memória foi liberada

    print("\nIs palindrome with pointers")
    print("Test 1")
    s6 = Stack()
    result = s6.is_palindrome_pointers("ana")
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True

    print("Test 2")
    result = s6.is_palindrome_pointers("arara")
    reuslt = s6.is_palindrome_pointers("arara")
    print("Result:", result)
    print("Expected: True")
    is_correct = is_correct and result is True

    print("Test 3")
    result = s6.is_palindrome_pointers("palindrome")
    print("Result:", result)
    print("Expected: False")
    is_correct = is_correct and result is False
    s6.free() # Sonha que a memória foi liberada

    print("\nOdds and Evens")
    print("Test 1")
    s7 = Stack()
    for i in range(1, 11):
        s7.push(i)
    odds, evens = s7.odds_and_evens()
    print("Result")
    print("Odds:")
    odds.print_stack()
    print("Evens:")
    evens.print_stack()
    print("Expected:")
    print("Odds:")
    for i in range(1, 11, 2):
        print(i)
    print("Evens:")
    for i in range(2, 11, 2):
        print(i)
    # Aqui não tem como comparar diretamente, então vamos comparar os topos e alturas
    is_correct = is_correct and odds.get_top() == 1 and evens.get_top() == 2 and odds.top_index == 4 and evens.top_index == 4

    print()
    if is_correct:
        print("All tests passed")
    else:
        print("Some tests failed")
    print("--------------------")
    return is_correct