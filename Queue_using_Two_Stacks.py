#!/bin/python3


class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, value):
        self.inbox.append(value)

    def dequeue(self):
        if len(self.outbox) == 0 and len(self.inbox) == 0:
            return None
        elif len(self.outbox) != 0:
            value = self.outbox.pop()
        else:
            self.outbox = self.inbox[::-1]
            self.inbox.clear()
            value = self.outbox.pop()

    def queue_print(self):
        if len(self.outbox) == 0 and len(self.inbox) == 0:
            return None
        if len(self.outbox) != 0:
            value = self.outbox[-1]
        else:
            value = self.inbox[0]

        print(value)


if __name__ == "__main__":

    queue = Queue()

    q = int(input().strip())

    for _ in range(q):
        query_input = list(map(int, input().strip().split()))
        query = query_input[0]

        if query == 1:
            value = query_input[1]
            queue.enqueue(value)
        elif query == 2:
            queue.dequeue()
        elif query == 3:
            queue.queue_print()
