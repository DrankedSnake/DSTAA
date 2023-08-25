from .node import Node


class Dequeue:
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

    def enqueue(self, item: int, side: str = "back") -> None:
        if side == "back":
            self.__enqueue_to_back(item)
        elif side == "front":
            self.__enqueue_to_front(item)
        else:
            raise Exception("Not existing operation")

    def dequeue(self, side: str = "front") -> int:
        if side == "front":
            return self.__dequeue_from_front()
        else:
            return self.__dequeue_from_back()

    def peek(self) -> int:
        return self.__head.value

    def is_empty(self) -> bool:
        return self.__length == 0

    def __enqueue_to_front(self, item: int) -> None:
        node = Node(item, None, None)

        if not self.__tail:
            self.__tail = node
        else:
            self.__head.previous = node

        prev_head = self.__head
        self.__head = node
        self.__head.next = prev_head

    def __enqueue_to_back(self, item: int) -> None:
        node = Node(item, None, None)

        if not self.__head:
            self.__head = node
        else:
            if self.__head is self.__tail:
                self.__tail.previous = self.__head
                self.__head.previous = None
            self.__tail.next = node
        prev_tail = self.__tail
        self.__tail = node
        self.__tail.previous = prev_tail

        self.__length += 1

    def __dequeue_from_front(self) -> int:
        if not self.__length:
            raise Exception("Queue is empty...")

        node = self.__head
        next_node = node.next
        self.__head = next_node
        self.__head.previous = None
        self.__length -= 1

        return node.value

    def __dequeue_from_back(self) -> int:
        if not self.__length:
            raise Exception("Queue is empty...")

        node = self.__tail
        previous_node = self.__tail.previous
        self.__tail = previous_node
        self.__tail.next = None
        self.__length -= 1

        return node.value
