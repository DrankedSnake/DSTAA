class Stack:
    def __init__(self, max_size: int) -> None:
        self.__top = 0
        self.__max_size = max_size
        self.__items = [None] * max_size
        self.__longest_item = 0

    def __str__(self) -> str:
        value = ""

        for item in self.__items:
            line = f"{item if item else ''}".center(self.__longest_item, " ")
            value += f"|{line}|\n"

        return value

    def push(self, item: int) -> None:
        self.__items[self.__max_size - self.__top - 1] = item
        item_string_length = len(str(item))

        if self.__top == self.__max_size:
            raise Exception(
                f"Maximum size already was reached.\nMax size: {self.__max_size}"
            )

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
