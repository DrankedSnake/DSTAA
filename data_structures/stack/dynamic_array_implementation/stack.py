class Stack:
    def __init__(self) -> None:
        self.__top = 0
        self.__max_size = 1
        self.__items = [None] * self.__max_size
        self.__longest_item = 0

    def __str__(self) -> str:
        value = ""

        for item in self.__items:
            line = f"{item if item else ''}".center(self.__longest_item + 2, " ")
            value += f"|{line}|\n"

        return value

    def __reallocate_memory(self):
        items = self.__items
        self.__max_size *= 2
        self.__items = [None] * self.__max_size
        counter = 1
        index = -1

        for _ in range(len(items)):
            item = items[index]
            self.__items[self.__max_size - counter] = item

            counter += 1
            index -= 1

    def push(self, item: int) -> None:
        if self.__top == self.__max_size:
            self.__reallocate_memory()

        self.__items[self.__max_size - self.__top - 1] = item
        item_string_length = len(str(item))

        if self.__longest_item < item_string_length:
            self.__longest_item = item_string_length

        self.__top += 1

    def pop(self) -> int:
        if not self.__top:
            raise Exception(f"There are no elements in stack.")
        else:
            item = self.__items[self.__max_size - self.__top]
            self.__items[self.__max_size - self.__top] = None
            self.__top -= 1

        return item

    @property
    def is_empty(self) -> bool:
        return self.__top == 0
