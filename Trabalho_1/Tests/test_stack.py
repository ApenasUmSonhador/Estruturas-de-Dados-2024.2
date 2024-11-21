from setup_paths import setup
setup()  # Configura o caminho para acessar as classes

from Stack import Stack
def test_stack():
    stack = Stack(5)
    print("is empty: ", stack.is_empty())
    print("is full: ", stack.is_full())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_stack()
    print("is empty: ", stack.is_empty())
    print("is full: ", stack.is_full())
    stack.delete(3)
    stack.print_stack()
    stack.free()

    stack = Stack(5)
    print(stack.is_palindrome("12321"))
    stack.free()

    stack = Stack(5)
    print(stack.is_palindrome("12345"))
    stack.free()

    stack = Stack(5)
    odd_stack, even_stack = stack.odd_and_evens([1, 2, 3, 4, 5])
    odd_stack.print_stack()
    even_stack.print_stack()
    stack.free()
    odd_stack.free()
    even_stack.free()