# Check for duplicates in list and print the duplicates as a list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []

# Steps
# loop through the list
# count how many times a value occurs in list -> .count()
# check for duplicates

for value in some_list:
    if some_list.count(value) > 1 and value not in duplicate_list: # occurs more than once = duplicate
        duplicate_list.append(value) # and, if duplicate already exists in list, then don't add it

print(duplicate_list)