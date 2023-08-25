from __future__ import annotations
from typing import List


class Node:
    def __init__(self) -> None:
        self.__parent: Node = None
        self.__children: List[Node]

    @property
    def parent(self) -> Node:
        return self.__parent

    @parent.setter
    def parent(self, node: Node) -> Node:
        return self.__parent

    @property
    def children(self) -> List[Node]:
        return self.__children

    def add_child(self, node: Node) -> None:
        if len(self.__children) <= 2:
            self.__children.append(node)
        else:
            raise Exception("Binary search tree node support only 2 children.")
