# Hash table implementation and
# Collision resolution by Separate Chaining
# In Python, main list is hash table and linked list will be represented by a Tuple

class HashTable:

    def __init__(self):
        self.MAX = 50  # size of list
        self.my_list = [[] for i in range(self.MAX)]  # initialize all index of main list with another empty list
        # Each index of the hashtable (list) will have a new list
        # Tuple (key,value) will be stored in the new empty lists

    # HASH FUNCTION
    def get_hash(self, key):  # get hash index, by giving a key (string)
        hashSum = 0
        for char in key: # iterating through each character in key
            hashSum += ord(char) # if character is string, ord() converts it to ASCII digit
        return hashSum % self.MAX
    # if key is int, then return key%self.MAX

    def __setitem__(self, key, value):
        index = self.get_hash(key)  # retrieve hash index for a given key

        # key-value pair will be added as a tuple into the empty list. Tuples cannot be changed
        found = False  # check if key exists in hash table, initially false

        # if key already exists, collision occurs! modify key-value pair to include a new key-value pair
        for idx, element in enumerate(self.my_list[index]): # iterating through the linked list of that particular index
            # element contains (key,value) of the new list, element[0] =  key, element[1] = value
            if len(element) == 2 and element[0] == key:
                # if size of element is 2, because ASCII values will be 2 digits
                # and, if first index of element tuple is a key
                self.my_list[index][idx] = (key, value)
                found = True
                break

        # if key does not exist, then add as a new key-value pair (inserted as a tuple)
        if not found:
            self.my_list[index].append((key, value))

    def __getitem__(self, key):  # get value for a given key
        index = self.get_hash(key)

        # iterate through all values in the index
        for element in self.my_list[index]:  # returns linked list of an index
            # accessing element directly in new list
            if element[0] == key:
                return element[1]
        # if key is not found, python returns None by default (initial value)

    def __delitem__(self, key):
        index = self.get_hash(key)
        for idx, element in enumerate(self.my_list[index]):
            if element[0] == key:
                del self.my_list[index][idx]

    def display_hash(self):
        for i in range(len(self.my_list)):
            print("Idx:", i, end=" ")

            for j in self.my_list[i]:
                print("--->", end=" ")
                print(j, end=" ")

            print()


def main():
    t1 = HashTable()
    t1['march 6'] = 78  # python supports __setitem__(a,b). gives the feel of a dictionary
    t1['march 17'] = 459
    t1['dec 6'] = 102
    t1.display_hash()
    print(t1['march 6']) # python supports __getitem___(a)
    print(t1['march 17'])

    del t1['march 17']
    t1.display_hash()


if __name__ == '__main__':
    main()
