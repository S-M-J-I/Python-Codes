# Binary Search

def binary_search(my_list, key):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if key == my_list[mid]:
            return mid # return index of element found
        elif key > my_list[mid]: # search right sub-array
            low = mid + 1
        else:
            # key < my_list[mid], search left sub-array
            high = mid - 1

    return -1 # Not found


# Divide and Conquer Approach - Preferred

def binary_search_recursive(my_list, low, high, key):
    if low == high: # if single element in list
        if my_list[low] == key:
            return low
        elif low > high:
            return -1
    else:
        # if list is large (low<high)
        mid = (low + high) // 2
        if key == my_list[mid]:
            return mid
        elif key > my_list[mid]:
            return binary_search_recursive(my_list, mid + 1, high, key) # recursively search right sub-list
        else:
            return binary_search_recursive(my_list, low, mid - 1, key) # recursively search left sub-list

    return -1


my_list = [2, 9, 4, 6, 24, 76, 52, 17]
# at first list has to be sorted
my_list = sorted(my_list)
key = 4
flag = binary_search_recursive(my_list, 0, len(my_list) - 1, key)
if flag == -1:
    print("Not Found")
else:
    print(f"Element found at index = {flag}")

