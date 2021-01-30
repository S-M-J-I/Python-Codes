# Stack implementation using collection.deque - Preferred implementation
# print(dir(stack))  # shows all methods in deque

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        # insert item to top of stack
        self.container.append(item)

    def pop(self):
        # remove item from top of stack
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        else:
            return self.container.pop()

    def peek(self):
        # see item at top of stack
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0  # returns True

    def get_length(self):
        return len(self.container)


# ------- other functions -----
def reverse_stack():
    s2 = Stack()
    s2.push(9)
    s2.push(34)
    s2.push(78)
    s2.push(12)
    print(s2.container)

    s3 = Stack()  # take a temporary stack to hold reversed contents
    while not s2.is_empty():
        # while stack is not empty
        # pop from one stack, push to temp stack
        s3.push(s2.pop())
    print(s3.container)


def reverse_string(string):
    s4 = Stack()
    # insert the items to a stack
    for char in string:
        s4.push(char)

    # we wont take a temp stack to hold a reverse string
    # we will take an empty string instead, and append to that string
    reverse_str = ''
    while not s4.is_empty():
        reverse_str += str(s4.pop())
    return reverse_str


# Write a function in python that checks if paranthesis in the string are balanced or not.
# Possible parantheses are "{}',"()" or "[]"

# to match brackets e.g. () or {} or [], we will take a dictionary
# one ) will be key, another ( ,first bracket will be value
# then we match key-value pair

def is_match(char1,char2):
    match_dictionary = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    # match_dictionary[char1] - returns value at key char1
    return match_dictionary[char1] == char2

def parenthesis(string):
    s2 = Stack()
    for char in string:
        # at first, check for first bracket
        if char == '(' or char == '{' or char == '[':
            # if you get first bracket, push to stack
            s2.push(char)
        if char == ')' or char == '}' or char == ']':
            # check for 2nd bracket
            if s2.get_length() == 0:
                # stack is empty
                return False

            if not is_match(char, s2.pop()):
                # matching first brackets (using the 2nd bracket as a key)
                # if one match is wrong, end of program
                return False

    # if all match is found
    return True

def main():
    s1 = Stack()
    s1.push(9)
    s1.push(34)
    s1.push(78)
    s1.push(12)
    print(s1.container)

    reverse_stack()
    print(reverse_string("We will conquere COVI-19"))
    print()
    
    print(parenthesis("({a+b})"))
    print(parenthesis("))((a+b}{"))
    print(parenthesis("((a+b))"))
    print(parenthesis("((a+g))"))


if __name__ == "__main__":
    main()
