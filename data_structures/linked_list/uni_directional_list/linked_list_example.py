from node import Node


class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__length = 0

    @property
    def head(self) -> Node:
        return self.__head

    @property
    def tail(self) -> Node:
        return self.__tail

    @property
    def length(self):
        return self.__length

    def __str__(self) -> str:
        node = self.__head
        value = ""

        while node is not None:
            value += f"{node} => "
            node = node.next

        return value[: len(value) - 4]

    def insert_front(self, item: str) -> None:
        """
        Inserts item into linked list at the front of list O(1) time complexity
        """

        if not self.__tail:
            self.__tail = self.__head
        self.__head = Node(item, self.__head)
        self.__length += 1

    def insert_back(self, item: str) -> None:
        """
        Inserts node into the tail with O(1) time complexity
        """

        node = Node(item, None)
        self.__tail.next = node
        self.__tail = node
        self.__length += 1

    def remove(self, item: str) -> None:
        previous = None
        current = self.__head

        while current is not None:
            if current.value == item:
                if previous:
                    previous.next = current.next
                else:
                    self.__head = current.next
                self.__length -= 1
                break
            previous = current
            current = current.next

    def find(self, item: str):
        node = self.__head

        while node.value != item:
            node = node.next()

        return node

    def search(self, item: str) -> bool:
        node = self.__head
        while node is not None:
            if node.value == item:
                return True
            node = node.next()
        return False

    def get_item(self, n: int):
        node = self.__head

        if n == 0:
            return node.value

        while n:
            node = node.next()
            n -= 1

        return node.value
    
    def to_puml(self):
        start = "@startuml"
        end = "@enduml"
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

        puml = f"{start}\n{content}\n{end}"

        with open("linked_list.puml", "w") as file:
            file.write(puml)
