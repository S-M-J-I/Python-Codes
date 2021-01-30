import re

# Dynamic list

# Taking list of numbers as input to a list
def input_items(my_list):
    try:
        input_list = input("Enter a list of numbers = ") # separated by space
        my_list = input_list.split()
        my_list = list(map(int, my_list)) # convert from str list to int list
        return my_list
    except ValueError as ex:
        print(repr(ex))


# Taking list of string (e.g.names) as input to a list
def input_strings(my_list):
    try:
        input_list = input("Enter a list of numbers = ") # seperated by comma
        my_list = input_list.split(',')
        # LATER - learn regex, then dont allow any string with digit -> use list(filter(re.match,))
        return my_list
    except TypeError as ex:
        print(repr(ex))


my_list = []
my_list = input_items(my_list)
print(my_list)

new_list = []
new_list = input_strings(new_list)
print(new_list)
