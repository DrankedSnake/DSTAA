from typing import Union
from node import Node


class Tree:
    def __init__(self) -> None:
        self.__root: Node = None
        self.__str_repr = ""

    def add_node(self, item: int, node: Node = None) -> None:
        if not self.__root:
            self.__root = Node(item, None, None)
        else:
            root = self.__get_root(node)
            if item < root.value:
                self.__add_left(item, root)
            else:
                self.__add_right(item, root)

    def search(self, item: int, node: Node = None):
        root = self.__get_root(node)

        if root.value == item:
            return True
        else:
            if item < root.value:
                return self.__search_left(item, root)
            if item > root.value:
                return self.__search_right(item, root)

    def __get_root(self, node: Node) -> Union[Node, None]:
        if not node:
            return self.__root
        else:
            return node

    def __add_left(self, item: int, node: Node) -> None:
        if root := node.left:
            self.add_node(item, root)
        else:
            node.left = Node(item, None, None)

    def __add_right(self, item: int, node: Node) -> None:
        if root := node.right:
            self.add_node(item, root)
        else:
            node.right = Node(item, None, None)

    def __search_left(self, item: int, node: Node) -> bool:
        if item < node.value:
            if node.left:
                return self.search(item, node.left)
            else:
                return False

    def __search_right(self, item: int, node: Node):
        if node.right:
            return self.search(item, node.right)
        else:
            return False

    def to_puml(self):
        start = "@startuml"
        end = "@enduml"
        content = f"{self.__str_repr}\n{self.__root.to_puml()}\n"
        nodes = []
        relations = []

        for line in content.split("\n"):
            if line.startswith("object"):
                nodes.append(line)
            else:
                relations.append(line)

        content = "\n".join(nodes)
        content += "\n".join(relations)

        puml = f"{start}\n{content}{end}"

        with open("tree.puml", "w") as file:
            file.write(puml)
