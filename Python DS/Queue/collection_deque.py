# Queue implementation using collection.deque - FIFO
# print(dir(stack))  # shows all methods in deque

from collections import deque


class Queue:

    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        # add item to left side of queue (first in)
        self.container.appendleft(item)

    def deque(self):
        # remove item from right of queue (first out)
        if self.is_empty():
            raise IndexError("Queue is Empty!")
        else:
            return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0  # checks if queue has items

    def get_length(self):
        return len(self.container)

    def front_element(self):
        # return element at front side (right side) of queue
        return self.container[-1]


# a program to print binary numbers from 1 to 10 using Queue. Use the Queue class
def binary_numbers(num):
    q2 = Queue()
    q2.enqueue("1")  # add the first binary number to queue
    # because binary of 1 == 1

    # add the rest of the binary numbers
    for i in range(num + 1):
        # with each iteration, 0 or 1 is added to a binary number

        # get the front element => binary number will be added to front
        # in order to get a new binary number
        front = q2.front_element()
        print(" ", front)

        # add 0 and 1 to front binary digit => the next 2 binary numbers
        q2.enqueue(front + "0")  # front contains a string, so append to a string
        q2.enqueue(front + "1")

        q2.deque() # remove the first element
        # why? - to get a new front and later a new binary number


def main():
    q1 = Queue()
    # add a dictionary to a queue
    q1.enqueue({
        'company': 'BMW',
        'Color': 'Blue',
        'Model_date': 2020
    })

    q1.enqueue({
        'company': 'Ferrari',
        'Color': 'Red',
        'Model_date': 2016
    })
    q1.enqueue({
        'company': 'Buggati',
        'Color': 'Grey Black',
        'Model_date': 2017
    })

    # print(q1.container)
    q1.deque()
    # print(q1.container)
    binary_numbers(10)


if __name__ == "__main__":
    main()
