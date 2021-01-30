# INHERITANCE AND POLYMORPHISM - IMP EXAMPLE

class Person:

    # Set type for the variables (better), and you can set default values
    def __init__(self,person_name: str,year_of_birth: int):
        self.__person_name = person_name
        self.__year_of_birth = year_of_birth

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
        return f"Person => Name = {self.__person_name}, YOB = {self.__year_of_birth}"

class Student(Person):

    def __init__(self,person_name:str,year_of_birth:int,email_id:str,student_id:str):
        super().__init__(person_name,year_of_birth) # call parent class constructor
        self.email_id = email_id
        self.student_id = student_id

    # override method from parent class
    def person_details(self):
        return f"Student => Email = {self.email_id} , ID - {self.student_id}"

    # if we directly want to print object details (without mentioning method again and again)
    # we will override dunder methods (__example__)

    def __str__(self):
        return f"Email = {self.email_id} , ID - {self.student_id}"

    #This dunder method helps in debugging (representing object)
    def __repr__(self):
        return f"Email = {self.email_id} , ID - {self.student_id}"


s1 = Student("Jawwad",1998,"jk@hotmail.com","EK564")
print(s1.person_details())
print(s1) # print object details (overwrite dunder methods)
print()

class Teacher(Person):

    def __init__(self,person_name:str,year_of_birth:int,department:str):
        super().__init__(person_name, year_of_birth)
        self.department = department

    def person_details(self):
        return f"Teacher => Department = {self.department}"


# creating a list to store 3 different objects
university_list = [
    Person("Jawwad",1998),
    Student("Jackson",1996,"jk@hotmail.com","DK987"),
    Teacher("Mary",1998,"CSE")
]

# iterating over the list
for people in university_list:
    print(people.person_details())


