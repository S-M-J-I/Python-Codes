# Dictionary example

#1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age':20,
    'username':'Skyabyss',
    'weapons':['pistol','shotgun','rifle','assault-rifle'],
    'is_active':True,
    'clan':'Grimhold Reapers'
}

#2 iterate and print all the keys in the above user.
print(user_profile.keys())
print()

#3 Add a new weapon to your user

# list value in weapons key
user_profile['weapons'].append("knife") # accessing key, then list

#4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({"is_banned":False})

#5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

#6 create a new user2 my copying the previous user and update the age value and username value.
user_profile2 = user_profile.copy()
user_profile2.update({
    "age":25,
    "username":"Clairant"
})

print(user_profile)
print()
print(user_profile2)
