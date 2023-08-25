from .node import Node


class Queue:
    def __init__(self) -> None:
        self.__head: Node = None
        self.__tail: Node = None
        self.__length = 0

    def __str__(self) -> str:
        value = "["

        node = self.__head

        while node:
            value += f"{node.value}, "
            node = node.next

        return value[: len(value) - 2] + "]"

    def enqueue(self, item: int) -> None:
        node = Node(item, None)

        if not self.__head:
            self.__head = node
        else:
            self.__tail.next = node
        self.__tail = node

        self.__length += 1

    def dequeue(self) -> int:
        if not self.__length:
            raise Exception("Queue is empty...")

        node = self.__head
        self.__head = node.next
        self.__length -= 1

        return node.value

    def peek(self) -> int:
        return self.__head

    def is_empty(self) -> bool:
        return self.__length == 0
