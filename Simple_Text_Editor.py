#!/bin/python3


class Editor:
    def __init__(self):
        self.undo = []
        self.text = ""

    def h_append(self, W):
        self.undo.append(self.text)
        self.text += W

    def h_delete(self, k):
        self.undo.append(self.text)
        self.text = self.text[: k * -1]

    def h_print(self, k):
        print(self.text[k - 1])

    def h_undo(self):
        self.text = self.undo.pop()


if __name__ == "__main__":

    ed = Editor()
    Q = int(input().rstrip())

    for _ in range(Q):
        op = input().strip().split()
        if op[0] == "1":
            ed.h_append(op[1])
        elif op[0] == "2":
            ed.h_delete(int(op[1]))
        elif op[0] == "3":
            ed.h_print(int(op[1]))
        elif op[0] == "4":
            ed.h_undo()
