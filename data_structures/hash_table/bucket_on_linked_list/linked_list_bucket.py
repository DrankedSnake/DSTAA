from node import Node


class LinkedListBucket:
    def __init__(self) -> None:
        self.__head = None
        self.__length = 0

    @property
    def head(self) -> Node:
        return self.__head

    @property
    def length(self):
        return self.__length

    def insert(self, value: int) -> None:
        node = Node(value)

        if not self.__head:
            self.__head = node
        else:
            old_head = self.__head
            self.__head = node
            self.__head.next = old_head

    def to_puml(self):
        content = self.__head.to_puml()
        nodes = []
        relations = []

        for line in content.split("\n"):
            if line.startswith("object"):
                nodes.append(line)
            else:
                relations.append(line)

        content = "\n".join(nodes) + "\n"
        content += "\n".join(relations)

        return content
