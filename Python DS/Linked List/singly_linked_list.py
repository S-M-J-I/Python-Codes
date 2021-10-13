# Linked List Implementation (from Scratch)
# Singly Linked List Implementation

class Node:
    # Node class which represents individual element in the linked list
    def __init__(self, data=None):
        # class members
        self.data = data
        self.next = None  # pointer to next element


class SinglyLinkedList:
    def __init__(self):
        # creating an empty linked list first for each object
        self.head = None  # points to head of linked list
        self.size = 0  # size will keep track of no.of elements in list

    # ------------------ Insertion into Singly Linked List --------------------------

    def insert_at_beginning(self, data):  # O(1) - preferred insertion
        node = Node(data)  # create a node
        
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_at_end(self, data):  # O(n)
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size += 1
        else:
            # if list is not empty, traverse list to reach the end
            itr = self.head
            while itr.next:  # if next value is available (loop goes on until next=None)
                itr = itr.next  # traversing nodes

            # now we are end node since itr.next = None
            itr.next = node
            self.size += 1

    def insert_by_index(self, index, data):  # O(n)
        # insert element at any index - O(n)

        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid Index")

        count = 0  # we need to maintain count to reach that particular index
        itr = self.head
        while itr:
            if count == index - 1:  # stop at previous element
                node = Node(data)
                node.next = itr.next
                itr.next = node
                self.size += 1
                break
            itr = itr.next
            count += 1

    def insert_by_value(self, value_after, data):  # O(n)
        # insert element after any value - O(n)
        # we will search for value by iterating through linked list

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head == value_after:
            # if only one element present (head), insert new node after head
            node = Node(data)
            self.head.next = node
            self.size += 1
            return

        itr = self.head
        while itr:
            # itr is another name for node, so itr.data is okay
            if itr.data == value_after:  # if iteration data == data in linked list
                node = Node(data)
                node.next = itr.next
                itr.next = node
                self.size += 1
                break
            itr = itr.next

    # ---------------- Deletion from Singly Linked List ------------------------

    def remove_at_beginning(self):  # O(1)
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            self.head = self.head.next  # change name of node
            self.size -= 1  # python has automatic garbage collection

    def remove_node_by_index(self, index):
        # remove element at any index - O(1)/O(n)

        # at first, validate index (check if index exists)
        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid Index")

        # if only one element is present - head element (remove beginning element)
        if index == 0:
            self.head = self.head.next  # change name of node
            self.size -= 1
        else:
            count = 0  # we need to maintain count to reach that particular index
            itr = self.head
            while itr:
                # we have to stop at the element prior (previous element) to the element we have to remove
                # because, we have to modify the links in order to delete
                if count == index - 1:  # stop at element before the element to be deleted
                    itr.next = itr.next.next  # change connection # next.next will be the element after deletion element
                    break
                # otherwise, keep iterating
                itr = itr.next
                count += 1
            self.size -= 1

    def remove_node_by_value(self, value):
        # remove element by any value - O(1)/O(n)
        # remember - we are accessing value inside node

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.data == value:  # if data to be deleted is at beginning node
            self.head = self.head.next  # change name of node
            self.size -= 1
        else:
            itr = self.head
            while itr.next:  # keep checking if next node is available (do remember we are in current node)
                if itr.next.data == value:  # if the data of NEXT node is equal to the value we are trying to delete
                    # (remember) we are current node
                    itr.next = itr.next.next  # change connection of current node to next.next
                    break
                # otherwise, keep iterating
                itr = itr.next
            self.size -= 1

    # ----------------- Other Operations - Traversal, Reverse, Search, etc -------------------

    def get_length(self):  # 0(1)
        return self.size

    def search_node_by_index(self, index):
        # return value found at searched index - O(n)

        if index < 0 or index >= self.get_length():
            raise ValueError("Index out of bounds")

        if index == 0:  # if index is present in first node
            return self.head.data
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index:
                    break
                itr = itr.next
                count += 1
            return itr.data

    def search_node_by_value(self, value):
        if self.head is None:
            print("Linked List is empty")
            return

        # Note: - Binary Search is difficult to implement in linked list

        # Linear Search - O(n)/O(1)
        flag = 0

        if self.head.data == value:  # if value is present in first node
            flag = 1
            return flag
        else:
            itr = self.head
            while itr:
                if itr.data == value:
                    flag = 1
                    break  # no need to search further
                itr = itr.next
            return flag

    def reverse_linked_list(self):  # O(n)
        # we need 3 pointers
        # 1) self.head, 2) new 3) prev
        # we will iterate through the loop and do the following

        prev = None
        itr = self.head
        while itr:  # this means => itr is not None
            new = itr.next  # before changing next of itr, store next node
            itr.next = prev  # actual reversing (change connections)
            prev = itr  # move prev one step forward
            itr = new  # move itr one step forward
        self.head = prev  # last element is now head

    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        # Iterate over the elements in linked list - 0(n)
        itr = self.head  # mark the beginning of linked list # create iterable object
        # itr has access to node which contains data and next address (itr.data, itr.next)
        linked_string = ''  # for displaying list
        while itr:
            linked_string = linked_string + str(itr.data) + " ---> "  # append to string
            itr = itr.next  # go to next element

        print(f"{linked_string}{'None'}")


def main():
    list1 = SinglyLinkedList()
    list1.insert_at_beginning(5)
    list1.insert_at_beginning(34)
    list1.insert_at_beginning(48)
    list1.insert_at_beginning(2)
    list1.insert_at_end(10)
    list1.insert_at_end(100)
    list1.print_list()
    print(f"Length = {list1.get_length()}")
    print()

    list1.reverse_linked_list()
    list1.print_list()
    print(f"Length = {list1.get_length()}")


if __name__ == '__main__':
    # if file is main (current) file, then call main function
    main()
