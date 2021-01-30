# Linear Search

def linear_search(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            return 1
    return -1


def linear_search_recursive(my_list, key, i):
    n = len(my_list)
    if i > n:  # at last index
        return -1
    if my_list[i] == key:
        return 1

    return linear_search_recursive(my_list, key, i+1)


my_list = [2, 9, 4, 6, 24, 76, 52, 17]
key = 17
flag = linear_search_recursive(my_list, key, 0)
if flag == 1:
    print("Found")
else:
    print("Not Found")
