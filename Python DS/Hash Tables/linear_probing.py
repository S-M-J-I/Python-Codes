# Hash table implementation and
# Collision resolution by Linear Probing

class HashTable:

    def __init__(self):
        self.MAX = 25  # size of list
        # we will use 2 lists. One list to store key, and another list to store corresponding value
        self.keys = [None] * self.MAX
        self.data = [None] * self.MAX

    def get_hash(self, key):  # get hash index, by giving a key (string)
        hashSum = 0
        for char in key:  # iterating through each character in key
            hashSum += ord(char)  # if character is string, ord() converts it to ASCII digit
        return hashSum % self.MAX

    # if key is int, then return key%self.MAX

    def re_hash(self, hash_index):
        # Linear Probing - i=0,1,2,3,4...
        new_hashSum = (hash_index + 1) % self.MAX
        return new_hashSum
    # Note: - Quadratic Probing => step.inc = 1
    # step.inc +=1
    # new_hashSum = (hash_index + step.inc*step.inc % self.MAX

    def __setitem__(self, key, value):
        hashIndex = self.get_hash(key)  # retrieve hash index for a given key

        if self.keys[hashIndex] is None:  # if empty slot available, then add key-value pair
            self.keys[hashIndex] = key
            self.data[hashIndex] = value
        elif self.keys[hashIndex] == key:  # if a slot contains already existing key
            self.data[hashIndex] = value  # old data is replaced with a new value
        else:
            new_hashIndex = self.re_hash(hashIndex)  # if empty slot is not found,
            while self.keys[new_hashIndex] is not None and self.keys[hashIndex] != key:  # if slot is not empty
                # and key from list != given key
                new_hashIndex = self.re_hash(hashIndex)  # re-hash until empty slot is found

            # same process again
            if self.keys[new_hashIndex] is None:
                self.keys[new_hashIndex] = key
                self.data[new_hashIndex] = value
            elif self.keys[new_hashIndex] == key:
                self.data[new_hashIndex] = value  # replace
            else:
                # if no slots are left
                raise KeyError("HashTable is Full")

    def __getitem__(self, key):  # get value for a given key
        hashIndex = self.get_hash(key)  # retrieve hash index for a given key
        data_found = None
        idx = hashIndex  # store the initial hashIndex (as comparison)

        while self.keys[idx] is not None:  # if slot is not empty, keep searching
            if self.keys[idx] == key:
                data_found = self.data[idx]
                break
            else:
                idx = self.re_hash(hashIndex)  # if not found in initial key, re-hash to search in another key
                if idx == hashIndex:
                    # search will terminate by checking to make sure that we have not returned to the beginning key.
                    # If that happens, we have exhausted all possible slots and the item must not be present.
                    break
        return data_found

    def __delitem__(self, key):
        hashIndex = self.get_hash(key)  # retrieve hash index for a given key
        idx = hashIndex  # store the initial hashIndex (as comparison)

        while self.keys[idx] is not None:  # if slot is not empty, keep searching
            if self.keys[idx] == key:
                del self.keys[idx]
                del self.data[idx]
                break
            else:
                idx = self.re_hash(hashIndex)  # if not found in initial key, re-hash to search in another key
                if idx == hashIndex:
                    # search will terminate by checking to make sure that we have not returned to the beginning key.
                    break

    def display_hash(self):
        print("KEY---VALUE")
        for i in range(len(self.data)):
            print(self.keys[i], "---", self.data[i])


def main():
    t1 = HashTable()
    t1['march 6'] = 78  # python supports __setitem__(a,b). gives the feel of a dictionary
    t1['march 17'] = 459
    t1['dec 6'] = 102
    t1['dec 6'] = 103
    t1.display_hash()
    print()
    print()
    del t1['march 17']
    t1.display_hash()


if __name__ == '__main__':
    main()
