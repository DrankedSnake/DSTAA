from custom_queue.fixed_array_implementaion.simple_array.queue import Queue


if __name__ == "__main__":
    queue = Queue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print(queue)
    print(queue.dequeue())
    print(queue)
