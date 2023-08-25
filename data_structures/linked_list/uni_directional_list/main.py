from linked_list_example import LinkedList


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_front("John")  # O(1)
    linked_list.insert_front("Marta")
    linked_list.insert_front("James")
    linked_list.insert_front("Amanda")
    linked_list.insert_front("Sam")
    linked_list.insert_back("Alex")  # O(1)

    linked_list.to_puml()
