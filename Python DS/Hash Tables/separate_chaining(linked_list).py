# Hash table implementation and
# Collision resolution by Separate Chaining

# Singly Linked List Implementation

class Node:
    # Node class which represents individual element in the linked list
    def __init__(self, key, data):
        # elements in hash table are in key-value pair
        # so nodes will have a key, as well as a value
        self.key = key
        self.data = data
        self.next = None


class HashTable:
    def __init__(self):
        self.MAX = 5
        self.hash_table = [None] * self.MAX  # hash table (main list)
        self.head = None
        self.size = 0  # count number of elements in linked list
        # each index of hash table will contain a linked list

    # HASH FUNCTION
    def hash(self, key):  # get hash index, by giving a key (string)
        hashSum = 0
        for char in key:  # iterating through each character in key
            hashSum += ord(char)  # if character is string, ord() converts it to ASCII digit
        return hashSum % self.MAX

    # if key is int, then return key%self.MAX

    def insert(self, key, data):

        index = self.hash(key)  # get hash index of key

        self.head = self.hash_table[index]  # Go to the first node corresponding to the hash index

        # if node is empty, it means hash table index is also empty
        if self.head is None:
            # Create a node, add it, return
            self.hash_table[index] = Node(key, data)
            self.size += 1
        else:
            # if a node is present, then Collision occurs!
            # Iterate to the end of the linked list and add a new node there
            itr = self.head
            while itr.next:  # if next value is available (loop goes on until next=None)
                itr = itr.next  # traversing nodes

            # now we are end node since itr.next = None
            itr.next = Node(key, data)
            self.size += 1

    def find(self, key):

        index = self.hash(key)
        self.head = self.hash_table[index]  # Go to the first node corresponding to the hash index

        # Traverse the linked list (at the table index) from this node
        itr = self.head

        while itr and itr.key != key:  # itr is not None and
            itr = itr.next  # keep traversing

        if itr is None:  # Not found
            return None
        else:
            # Found - return the data data
            return itr.data

    def remove(self, key):  # something wrong here - rewrite logic urself

        index = self.hash(key)
        self.head = self.hash_table[index]  # Go to the first node corresponding to the hash index

        itr = self.head
        prev = None  # to keep track of previous node

        while itr and itr.key != key:  # itr is not None and
            prev = itr
            itr = itr.next  # keep traversing

        if itr is None:  # Not found
            return None
        else:
            # Key found - return the data data
            result = itr.data  # store the data to be removed
            prev.next = prev.next.next  # remove the node from linked list

            # prev.next.next can be either None or another node

            return result

    def display_hash(self):
        for i in range(len(self.hash_table)):
            print(i, "=>", end=" ")

            self.head = self.hash_table[i]  # Go to the first node corresponding to the hash index

            itr = self.head  # mark the beginning of linked list # create iterable object

            # itr has access to node which contains data and next address (itr.key, itr.data, itr.next)
            linked_string = ''  # for displaying list
            while itr:
                linked_string = linked_string + "[" + str(itr.key) + ":" + str(
                    itr.data) + "]" + " ---> "  # append to string
                itr = itr.next  # go to next element

            print(f"{linked_string}{'None'}")


def main():
    ht = HashTable()
    ht.insert("A", "17")  # key-value pair
    ht.insert("F", "85")  # key-value pair
    ht.insert("B", "29")  # key-value pair
    ht.insert("C", "222")  # key-value pair

    print(ht.find("A"))
    ht.display_hash()
    print()

    element_removed = ht.remove("F")
    print(f"Element data removed = {element_removed}")
    ht.display_hash()


if __name__ == '__main__':
    main()
