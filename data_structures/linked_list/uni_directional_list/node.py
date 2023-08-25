from __future__ import annotations


class Node:
    def __init__(self, value: str, next_node: Node):
        self.__value = value
        self.__next = next_node

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next: Node):
        self.__next = next

    def __str__(self):
        return f"| {self.value} |"

    def to_puml(self) -> str:
        repr = f"object {self.value}\n"

        if self.next:
            repr += f"{self.value} -right-> {self.next.value}\n"
            repr += f"{self.next.to_puml()}"

        return repr
