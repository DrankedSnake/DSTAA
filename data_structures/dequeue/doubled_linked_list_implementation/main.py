from custom_dequeue.doubled_linked_list_implementation.dequeue import Dequeue


if __name__ == "__main__":
    dequeue = Dequeue()
    dequeue.enqueue(1, "front")
    dequeue.enqueue(2, "back")
    dequeue.enqueue(3, "front")
    dequeue.enqueue(4, "back")
    print(dequeue)
    print(dequeue.dequeue("front"))
    print(dequeue)
    print(dequeue.dequeue("back"))
    print(dequeue)
