class PyList:
    # creating a list from scratch (with basic operations)
    # can add more methods later

    def __init__(self):
        # create an empty list with each new object
        self.my_list = []

    def __iter__(self):
        # The yield call in Python suspends the execution of the __iter__ method
        # and returns the yielded item to the iterator.
        for i in range(self.list_length()):
            yield self.my_list[i]

    def initialize_list(self):
        # input a list of numbers with space
        input_string = input("Enter a list of numbers = ")
        str_list = input_string.split()
        self.my_list = list(map(int, str_list))

    def add_item(self, item):
        self.my_list.append(item)

    def insert_item(self, index, value):
        self.my_list.insert(index, value)

    def list_length(self):
        return len(self.my_list)

    def get_item(self, index):
        if 0 <= index < self.list_length():  # index >= 0 and index < self.list_length():
            return self.my_list[index]
        raise IndexError("PyList index is out of range")

    def set_item(self, index, value):
        # change a value in an index
        self.my_list[index] = value

    def pop_item(self, index):
        if not index:  # if index is empty (index = None)
            self.my_list.pop()  # pop from end
        else:
            self.my_list.pop(index)


def main():
    list1 = PyList()
    list1.initialize_list()
    print(f"Original list = {list1.my_list}")
    list1.insert_item(1, 100)
    list1.pop_item(None)

    list_iter = iter(list1.my_list)
    for i in list_iter:
        print(i, end=" ")
    print()


if __name__ == '__main__':
    # if file is main (current) file, then call main function
    main()
