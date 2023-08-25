from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node, previous: Node) -> None:
        self.__value = value
        self.__next = next
        self.__previous = previous

    @property
    def next(self) -> Node:
        return self.__next

    @next.setter
    def next(self, node: Node) -> None:
        self.__next = node

    @property
    def previous(self) -> Node:
        return self.__previous

    @previous.setter
    def previous(self, node: Node) -> None:
        self.__previous = node

    @property
    def value(self) -> int:
        return self.__value
