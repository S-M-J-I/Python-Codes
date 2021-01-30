# Doubly Linked List Implementation

class Node:
    # Node class which represents individual element in the linked list
    def __init__(self, data=None):
        # class members
        self.data = data
        self.next = None  # pointer to next element
        self.prev = None  # pointer to previous element


class DoublyLinkedList:
    def __init__(self):
        # creating an empty linked list first for each object
        self.head = None  # points to head of linked list
        self.tail = None  # points to end of linked list
        self.size = 0  # size will keep track of no.of elements in list

    # ------------------ Insertion into Doubly Linked List --------------------------

    def insert_at_beginning(self, data):  # O(n)
        node = Node(data)  # create a node
        if self.head is None and self.tail is None:  # if list is initially empty
            # mark the beginning node as head node and tail node
            self.head = node
            self.tail = node
            self.size += 1  # one element added
        else:
            # adding another node to beginning (list is not empty)
            self.head.prev = node  # connect head.prev backwards to node
            node.next = self.head  # connect node.next forward to head
            self.head = node  # change name of node to head (store)
            self.size += 1

    def insert_at_end(self, data):  # O(n)
        node = Node(data)  # create a node
        if self.head is None and self.tail is None:  # if list is initially empty
            # mark the beginning node as head node and tail node
            self.head = node
            self.tail = node
            self.size += 1  # one element added
        else:
            # adding another node to end (list is not empty)
            self.tail.next = node  # connect tail.next forwards to node
            node.prev = self.tail  # connect node.prev backwards to head
            self.tail = node  # change name of node to tail (store)
            self.size += 1

    def insert_by_index(self, index, data):  # O(n)
        # insert element at any index - O(n)

        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
        else:
            count = 0  # we need to maintain count to reach that particular index
            itr = self.head
            while itr:
                if count == index - 1:  # stop at previous element
                    node = Node(data)
                    node.next = itr.next  # change connections
                    itr.next.prev = node
                    itr.next = node
                    node.prev = itr
                    itr.next = node  # rename(store) node [new node in between will be itr.next]
                    self.size += 1
                    break
                itr = itr.next
                count += 1

    def insert_by_value(self, value_after, data):  # O(n)
        # insert element after any value - O(n)
        # we will search for value by iterating through linked list

        if self.head is None and self.tail is None:
            self.insert_at_beginning(data)
        else:
            itr = self.head
            while itr:
                # itr is another name for node, so itr.data is okay
                if itr.data == value_after:  # if iteration data == data in linked list
                    node = Node(data)
                    node.next = itr.next  # change connections
                    itr.next.prev = node
                    itr.next = node
                    node.prev = itr
                    itr.next = node  # rename(store) node [new node in between will be itr.next]
                    self.size += 1
                    break
                itr = itr.next

    # ---------------- Deletion from Doubly Linked List ------------------------
    def remove_at_beginning(self):  # O(1)
        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return
        else:
            if self.head.prev is None:
                self.head = self.head.next  # change name of node (just one change is enough)
                self.head.prev = None
                self.size -= 1  # python has automatic garbage collection

    def remove_at_end(self):  # O(n)
        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return
        else:
            if self.tail.next is None:
                self.tail = self.tail.prev  # change name of node (just one change is enough)
                self.tail.next = None
                self.size -= 1  # python has automatic garbage collection

    def remove_node_by_index(self, index):
        # remove element at any index - O(1)/O(n)

        # at first, validate index (check if index exists)
        if index < 0 or index >= self.get_length():
            raise ValueError("Invalid Index")

        # if only one element is present - head element (remove beginning element)
        if index == 0:
            self.remove_at_beginning()
        elif index == self.get_length() - 1:
            self.remove_at_end()
        else:
            count = 0  # we need to maintain count to reach that particular index
            itr = self.head
            while itr:
                # we have to stop at the element prior (previous element) to the element we have to remove
                # because, we have to modify the links in order to delete
                if count == index - 1:  # stop at element before the element to be deleted
                    itr.next = itr.next.next  # change connection # next.next will be the element after deletion element
                    itr.next.prev = itr  # connect backwards connection as well
                    break
                # otherwise, keep iterating
                itr = itr.next
                count += 1
            self.size -= 1

    def remove_node_by_value(self, value):
        # remove element by any value - O(1)/O(n)
        # remember - we are accessing value inside node

        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return

        if self.head.data == value:  # if data to be deleted is at beginning node
            self.remove_at_beginning()
        elif self.tail.data == value:
            self.remove_at_end()
        else:
            itr = self.head
            while itr.next:  # keep checking if next node is available (do remember we are in current node)
                if itr.next.data == value:  # if the data of NEXT node is equal to the value we are trying to delete
                    # (remember) we are current node
                    itr.next = itr.next.next  # change connection of current node to next.next
                    itr.next.prev = itr  # connect backwards connection as well
                    break
                # otherwise, keep iterating
                itr = itr.next
            self.size -= 1

    # ----------------- Other Operations - Traversal, Reverse, Search, etc -------------------

    def get_length(self):  # O(1)
        return self.size

    def search_node_by_index(self, index):
        # return value found at searched index - O(n)

        if index < 0 or index >= self.get_length():
            raise ValueError("Index out of bounds")

        if index == 0:  # if index is present in first node
            return self.head.data
        elif index == self.get_length() - 1:  # if index is present in last node
            return self.tail.data
        else:  # rest of the nodes
            count = 0
            itr = self.head
            while itr:
                if count == index:
                    break
                itr = itr.next
                count += 1
            return itr.data

    def search_node_by_value(self, value):
        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return

        # Note: - Binary Search is difficult to implement in linked list

        # Linear Search - O(n)
        flag = 0  # constant (initially 0)

        if self.head.data == value or self.tail.data == value:  # if value is present in first node or last node
            flag = 1
            return flag
        else:
            itr = self.head
            while itr:
                if itr.data == value:
                    flag = 1  # if found, flag = 1
                    break  # no need to search further
                itr = itr.next
            return flag

    def reverse_list(self):
        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return

        temp = None  # take temporary variable (pointer)
        itr = self.head
        while itr:
            # main reverse logic

            # swap next and prev pointers for the current node
            temp = itr.prev
            itr.prev = itr.next  # prev pointer points to next node
            itr.next = temp  # next pointer points to previous node
            temp = itr  # update the previous node before moving to the next node
            # move to the next node in the doubly linked list
            itr = itr.prev  # (advance using prev pointer since next & prev pointers were swapped)

        # update head pointer to the last node
        if temp:
            self.head = temp

    def print_list_forward(self):  # O(n)

        if self.head is None:
            print("Linked List is empty")
            # return nothing to calling function
            return

        # Iterate over the elements in linked list - 0(n)
        itr = self.head  # mark the beginning of linked list # create iterable object
        linked_string = ''  # for displaying list
        while itr:
            # append to string
            linked_string = linked_string + str(itr.data) + " ---> "
            itr = itr.next  # go to next element

        print(f"{'None <--- '}{linked_string}{'None'}")

    def print_list_backward(self):  # O(n)
        # print linked list  in reverse order

        if self.head is None and self.tail is None:
            print("Linked List is empty")
            return

        # Iterate over the elements in linked list - 0(n)
        itr = self.tail  # mark the ending of linked list # create iterable object
        linked_string = ''  # for displaying list
        while itr:
            # append to string
            linked_string = linked_string + str(itr.data) + " ---> "
            itr = itr.prev  # go to next element

        print(f"{'None <--- '}{linked_string}{'None'}")

    # -------------------------- New methods added for queue class ---------------------------

    def first_element_value(self):
        return self.head.data

    def last_element_value(self):
        return self.tail.data




