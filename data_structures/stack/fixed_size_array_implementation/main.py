from custom_stack.fixed_size_array_implementation.stack import Stack


if __name__ == "__main__":
    stack1 = Stack(5)
    stack2 = Stack(7)

    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(40)
    stack1.push(400)

    stack2.push(1000)
    stack2.push(100)
    stack2.push(10)
    stack2.push(1)
    print(stack2)

    print(stack1)
    print(stack1.pop())
    print(stack1)
    stack1.push(4000)
    print(stack1)

    stack1.pop()
    stack1.pop()
    stack1.pop()
    print(stack1)
