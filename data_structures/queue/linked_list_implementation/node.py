from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node) -> None:
        self.__value = value
        self.__next = next

    @property
    def next(self) -> Node:
        return self.__next

    @next.setter
    def next(self, node: Node) -> None:
        self.__next = node

    @property
    def value(self) -> int:
        return self.__value
