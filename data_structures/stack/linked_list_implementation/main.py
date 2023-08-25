from custom_stack.linked_list_implementation.stack import Stack


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack)
    stack.pop()
    print(stack)
