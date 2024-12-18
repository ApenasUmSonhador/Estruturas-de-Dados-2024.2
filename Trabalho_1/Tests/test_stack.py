from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Stack import Stack

import time

def test_stack_performance():
    print("--------------------")
    print("Test Stack Performance")

    print("\nPush")
    print("Test 1")
    s1 = Stack()
    time.start = time.time()
    s1.push(1)
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("Test 1000")
    s2 = Stack(1000)
    time.start = time.time()
    for i in range(1000):
        s2.push(i)
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("Test 1000000")
    s3 = Stack(1000000)
    time.start = time.time()
    for i in range(1000000):
        s3.push(i)
    time.end = time.time()
    print("Time:", time.end - time.start)
    
    print("\nPop")
    print("Test 1")
    time.start = time.time()
    s1.pop()
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("Test 1000")
    time.start = time.time()
    for i in range(1000):
        s2.pop()
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("Test 1000000")
    time.start = time.time()
    for i in range(1000000):
        s3.pop()
    time.end = time.time()
    print("Time:", time.end - time.start)

    s1.free(); s2.free(); s3.free() # Sonha que a memória foi liberada

    print("\nGet Top")
    s = Stack()
    s.push(1)
    time.start = time.time()
    s.get_top()
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("\nIs Empty")
    print("False")
    time.start = time.time()
    s.is_empty()
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("False")
    s.pop()
    time.start = time.time()
    s.is_empty()
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("\nIs Full")
    print("False")
    time.start = time.time()
    s.is_full()
    time.end = time.time()
    print("Time:", time.end - time.start)

    s.free() # Sonha que a memória foi liberada

    print("True")
    s = Stack(1)
    s.push(1)
    time.start = time.time()
    s.is_full()
    time.end = time.time()
    print("Time:", time.end - time.start)

    s.free() # Sonha que a memória foi liberada

    print("\nDelete")
    print("Test 1")
    s = Stack()
    s.push(0)
    time.start = time.time()
    s.delete(0)
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada

    print("Test 1000")
    s = Stack(1000)
    for i in range(1, 1001):
        s.push(i)
    time.start = time.time()
    s.delete(500)
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada


    print("Test 1000000")
    s = Stack(1000000)
    for i in range(1, 1000001):
        s.push(i)
    time.start = time.time()
    s.delete(500000)
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada

    print("\nIs Palindrome")
    print("True")
    s = Stack()
    time.start = time.time()
    s.is_palindrome("ararararara")
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("False")
    time.start = time.time()
    s.is_palindrome("palindrome")
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada

    print("\nIs Palindrome Pointers")
    print("True")
    s = Stack()
    time.start = time.time()
    s.is_palindrome_pointers("ararararara")
    time.end = time.time()
    print("Time:", time.end - time.start)

    print("False")
    time.start = time.time()
    s.is_palindrome_pointers("palindrome")
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada

    print("\nOdds and Evens")
    s = Stack()
    for i in range(1, 11):
        s.push(i)
    print("Test 1")
    time.start = time.time()
    s.odds_and_evens()
    time.end = time.time()
    print("Time:", time.end - time.start)
    s.free() # Sonha que a memória foi liberada

    print("--------------------")

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
