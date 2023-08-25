from custom_stack.linked_list_implementation.node import Node


class Stack:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__longest_item = 0

    def __str__(self) -> str:
        value = ""
        node = self.__head

        while node is not None:
            line = f"{node.value}".center(self.__longest_item + 2, " ")
            value += f"|{line}|\n"
            node = node.next

        return value

    def push(self, value: int) -> None:
        self.__head = Node(value, self.__head)
        item_str_length = len(str(value))

        if self.__longest_item < item_str_length:
            self.__longest_item = item_str_length

    def pop(self) -> int:
        if self.__head is None:
            raise Exception("Stack is empty")

        node = self.__head
        self.__head = node.next

        return self.__head.value
