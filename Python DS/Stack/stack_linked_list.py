# Stack implementation using Linked List

# To use a class of another file in current file, import it
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        self.stack_list = DoublyLinkedList()  # create an empty stack object
        # this object will contain nodes (doubly linked list)

    def push(self, item):
        # call methods in doubly linked list class
        self.stack_list.insert_at_end(item)

    def pop(self):
        # removing item added at last (top item - tail)
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            top_item = self.stack_list.last_element_value()
            self.stack_list.remove_at_end()
            return top_item

    def peek(self):
        # last item in list - tail
        return self.stack_list.last_element_value()

    def is_empty(self):
        # are there any elements in stack
        return self.stack_list.get_length() == 0  # length = 0 when stack has no items

    def __len__(self):
        # override built in len method - to suit your purposes
        return self.stack_list.get_length()


def main():
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.stack_list.print_list_forward()
    print(s1.peek())
    print(f"Length = {len(s1)}")  # use len(object) - due to being overridden

    print()
    s1.pop()
    print(s1.pop())
    print(s1.peek())
    print(f"Length = {len(s1)}")
    s1.stack_list.print_list_forward()


if __name__ == "__main__":
    main()
