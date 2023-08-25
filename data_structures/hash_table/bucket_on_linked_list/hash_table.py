from linked_list_bucket import LinkedListBucket


class HashTable:
    def __init__(self) -> None:
        self.__hashes = [None] * 10
        self.__length = 0
        self.__base = 10

    def insert(self, key: int, value: int) -> None:
        index = self.__hash(key)
        hash_item = self.__hashes[index]

        if not hash_item:
            self.__hashes[index] = value
        else:
            if isinstance(self.__hashes[index], LinkedListBucket):
                self.__hashes[index].insert(value)
            else:
                old_value = self.__hashes.pop(index)
                linked_list = LinkedListBucket()
                linked_list.insert(old_value)
                linked_list.insert(value)
                self.__hashes[index] = linked_list

    def find(self, key: int) -> int:
        item = self.__hashes[self.__hash(key)]

    def __hash(self, key: int) -> int:
        return key % self.__base

    def to_puml(self):
        start = "@startuml"
        end = "@enduml"
        puml = ""

        for index, item in enumerate(self.__hashes):
            if isinstance(item, LinkedListBucket):
                puml += f"object {index}_bucket\n"
            else:
                puml += f"object {index}_{item}\n"

        for index in range(len(self.__hashes)):
            if isinstance(item, LinkedListBucket):
                puml += item.to_puml()
            else:
                if index < self.__base - 1:
                    puml += f"{index}_{item} -down-- {index + 1}_{self.__hashes[index + 1]}\n"

        puml = f"{start}\n{puml}\n{end}"

        with open("hash_table_on_linked_list_bucket.puml", "w") as file:
            file.write(puml)
