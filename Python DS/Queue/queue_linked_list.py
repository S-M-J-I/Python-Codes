# Queue implementation using Linked List - preferred implementation

# To use a class of another file in current file, import it
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.queue_list = DoublyLinkedList()  # create an empty queue object
        # this object will contain nodes (doubly linked list)

    def enqueue(self, item):
        # call methods in doubly linked list class
        # add item to left side of queue (first in)
        self.queue_list.insert_at_beginning(item)

    def dequeue(self):
        # remove first item from queue (first out)
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            front_item = self.queue_list.last_element_value() # store front item before it is removed
            self.queue_list.remove_at_end()
            return front_item

    def front(self):
        # return element at front side (right side) of queue
        return self.queue_list.last_element_value()  # tail value

    # The concept can also be reversed (same thing btw)
    # such as, insert_at_end, remove_at_beginning, front -> head value

    def is_empty(self):
        # are there any elements in queue
        return self.queue_list.get_length() == 0  # length = 0 when queue has no items

    def __len__(self):
        # override built in len method - to suit your purposes
        return self.queue_list.get_length()


def main():
    q1 = Queue()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    q1.queue_list.print_list_forward()
    print(q1.front())
    print(f"Length = {len(q1)}")  # use len(object) - due to being overridden

    print()
    q1.dequeue()
    print(q1.dequeue())
    print(q1.front())
    print(f"Length = {len(q1)}")
    q1.queue_list.print_list_forward()
    print(q1.is_empty())


if __name__ == "__main__":
    main()
