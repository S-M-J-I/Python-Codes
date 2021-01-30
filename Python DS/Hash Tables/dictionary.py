dictionary = {
    'basket': [54, 241, 21, 95, 74],
    'age': 22
}

dictionary['age'] = 30 # set item at any key - O(1)
print(dictionary['basket'][0])  # accessing a value by key(index) - O(1)
print(f"length = {len(dictionary)}")  # O(1)
print(f"length of value = {len(dictionary['basket'])}")  # O(1) - length of ds (value) in a key

# look up operation
key1 = "basket"
if dictionary.get(key1, "key does not exist"):  # or if key in dictionary.keys() #  O(1)
    print(dictionary[key1])

# checking whether - true or false
print(dictionary.keys())  # returns a list of keys in the dictionary - O(n)
print('age' in dictionary.keys())  # check if key exists - O(1)

print(dictionary.values())  # returns a list of values in the dictionary - O(n)
print(36 in dictionary.values())  # check if value exists - O(1)

print(dictionary.items())  # grabs all the key-value pair and returns a tuple
# dictionary.clear() # O(1)
dictionary2 = dictionary.copy()
print(dictionary2)

value_removed = dictionary2.pop("age") # takes a key, and removes the key-value pair. the value removed is returned - O(1)
print(dictionary2)
print(value_removed)

# update()-> 1) if key exits, value is updated
# 2) if key does not exist, added as new entry (key-value pair)
# dictionary2.update({"age":40})
dictionary2.update({"username":"fidajisa"})
print()

# Iterating over keys
# iterating through a dictionary - O(n)
for item in dictionary.keys():
    print(item)

# Iterating over values
# iterating through a dictionary - O(n)
for item in dictionary.values():
    print(item)

# Iterating over key and values
# iterating through a dictionary - O(n)
for keys,values in dictionary.items():
    print(keys,"-",values)
