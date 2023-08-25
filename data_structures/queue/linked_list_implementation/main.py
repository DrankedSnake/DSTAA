from custom_queue.linked_list_implementation.queue import Queue


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    print(queue)
    print(queue.dequeue())
    print(queue)
