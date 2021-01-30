# functional programming example - map(),filter(),zip()

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# ------- ANSWER -------

# to capitalize - use upper()
def capitalize(item):
    return item.upper()

capitals = list(map(capitalize,my_pets))
print(capitals)


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

# ------- ANSWER -------
combined_sorted_list = list(zip(my_strings,sorted(my_numbers)))
print(combined_sorted_list)


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

# ------- ANSWER -------
def filter_score(marks):
    if marks>50:
        return marks

highest_scores = list(filter(filter_score,scores))
print(highest_scores)



