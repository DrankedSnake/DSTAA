class List:
    def __init__(self) -> None:
        self.__max_elements = 1
        self.__items = [None] * self.__max_elements
        self.__length = 0

    def __str__(self) -> str:
        value = "["

        for item in self.__items:
            if item:
                value += f"{item}, "

        return value[: len(value) - 2] + "]"

    def __reallocate_memory(self):
        self.__max_elements *= 2
        items = self.__items
        self.__items = [None] * self.__max_elements

        for index, item in enumerate(items):
            self.__items[index] = item

    def append(self, item: int) -> None:
        if self.__length == self.__max_elements:
            self.__reallocate_memory()

        self.__items[self.__length] = item
        self.__length += 1
