class Queue:
    def __init__(self, max_size: int) -> None:
        self.__max_size = max_size
        self.__items = [None] * self.__max_size
        self.__front_index = 0
        self.__rear_index = 0
        self.__length = 0

    def __str__(self) -> str:
        value = "["

        for item in self.__items:
            value += f"{item}, " if item else ""

        return value[: len(value) - 2] + "]"

    def enqueue(self, item: int) -> None:
        if self.__rear_index + 1 == self.__max_size:
            raise Exception("Queue is full...")

        self.__items[self.__rear_index] = item
        self.__rear_index += 1
        self.__length += 1

    def dequeue(self) -> int:
        item = self.__items[self.__front_index]
        self.__items[self.__front_index] = None
        next_item_index = 1

        for index in range(self.__length):
            self.__items[index] = self.__items[next_item_index]
            next_item_index += 1

        self.__length -= 1
        self.__rear_index -= 1

        return item
