#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_oldest_cat(self,*args):
        # *args because we need to compare all objects age variable
        return max(args)

# 1 Instantiate the Cat object with 3 cats
Lulu = Cat("Lulu",5)
Chuchu = Cat("Chuchu",7)
Momo = Cat("Momo",6)

# 2 Create a function that finds the oldest cat

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"Oldest cat is {Lulu.get_oldest_cat(Lulu.age,Chuchu.age,Momo.age)}")
