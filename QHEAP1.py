#!/bin/python3

class Heap:
    def __init__(self):
        self.heap = []

    def binary_search(self, v):
        low = 0
        high = len(self.heap) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = self.heap[mid]
            if guess == v:
                return mid
            elif guess > v:
                low = mid + 1
            else:
                high = mid - 1
        return mid

    def hadd(self, v):
        if len(self.heap) == 0:
            self.heap.append(v)
        elif v <= self.heap[-1]:
            self.heap.append(v)
        elif v >= self.heap[0]:
            self.heap.insert(0, v)
        else:
            idx = self.binary_search(v)
            while True:
                if v >= self.heap[idx]:
                    self.heap.insert(idx, v)
                    break
                idx += 1

    def hdelete(self, v):
        idx = self.binary_search(v)
        self.heap.pop(idx)

    def hprint(self):
        print(self.heap[-1])


if __name__ == "__main__":

    queue = Heap()

    q = int(input().strip())

    for _ in range(q):
        query_input = list(map(int, input().strip().split()))
        query = query_input[0]

        if query == 1:
            v = query_input[1]
            queue.hadd(v)
        elif query == 2:
            v = query_input[1]
            queue.hdelete(v)
        elif query == 3:
            queue.hprint()
