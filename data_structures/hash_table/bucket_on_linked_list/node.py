from __future__ import annotations


class Node:
    def __init__(self, value: int) -> None:
        self.__value = value
        self.__next: Node = None

    @property
    def next(self) -> Node:
        return self.__next

    @next.setter
    def next(self, node: Node) -> Node:
        self.__next = node

    @property
    def value(self) -> int:
        return self.__value

    def to_puml(self) -> str:
        repr = f"object {self.value}\n"

        if self.next:
            repr += f"{self.value} -right-> {self.next.value}\n"
            repr += f"{self.next.to_puml()}"

        return repr
