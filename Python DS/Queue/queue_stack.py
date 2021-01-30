# implement queue using stack (2 stacks)

# Queue implementation using collection.deque

from collections import deque


class Queue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def enqueue(self, item):
        # add item to queue (first in) - item will be added to stack1
        self.stack1.append(item)

    def deque(self):
        # remove item from queue
        # Steps written in notebook ****
        
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                return "Queue is Empty!"  # if stack1 and stack2 is empty, then queue is empty
            else:
                while len(self.stack1) != 0:
                    # Transfer all elements from stack1 to stack 2 (till stack1 is empty)
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()  # remove the top element(now it behaves like a queue)

    def is_empty(self, container):
        # to check if queue is empty, we need to check both stacks
        return len(self.stack1) and len(self.stack2)

    def get_length(self):
        # since queue is implement using 2 stacks
        # size of queue = size of stack1 + stack2
        return len(self.stack1) + len(self.stack2)


def main():
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print(q1.deque())
    print(q1.deque())
    print(q1.deque())
    print(q1.deque())


if __name__ == "__main__":
    main()
