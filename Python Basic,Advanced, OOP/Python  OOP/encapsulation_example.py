# ENCAPSUALTION - IMP EXAMPLE (+ TYPE, DEFAULT VALUES)

class Person:

    # Set type for the variables (better), and you can set default values
    def __init__(self,person_name: str,year_of_birth: int, height: int = None):
        self.__person_name = person_name
        self.__year_of_birth = year_of_birth
        self.__height = height

    def get_name(self):
        return self.__person_name

    def get_year_of_birth(self):
        return self.__year_of_birth

    # check if user has entered a valid name - replaced later with regular expressions
    def __has_any_number(self,name:str):
        return "0" in name

    def set_new_name(self,new_name:str):
        if self.__has_any_number(new_name):
            print("You are not allowed to set this name")
        self.__person_name = new_name

    def person_details(self):
        return f"Name = {self.__person_name}, YOB = {self.__year_of_birth}, Height = {self.__height if self.__height is not None else 'Invalid'}"

# creating a list - that stores objects
person_list = [
    Person("Jawwad",1998,56),
    Person("Mary",2000,48),
    Person("Moumy",1997),
    Person("Shafique",1956),
    Person("Jackson",1986,25)
]

# iterating through the list
for person in person_list:
    # person holds objects
    if person.get_year_of_birth() >= 1990:
        print(person.person_details())


