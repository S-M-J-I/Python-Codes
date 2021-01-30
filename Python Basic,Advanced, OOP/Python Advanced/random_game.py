import random
import sys

try:
    num1= int(sys.argv[1])
    num2= int(sys.argv[2])

    while True:
        print(f"Guess a number between {num1} and {num2}")
        number = int(input("Your number = "))
        if num1 <= number <= num2:
            random_num = random.randint(num1,num2)
            if number == random_num:
                print("You are a Genius")
                break
            else:
                print(f"Numbers do not match! Random Number Generated was {random_num}")

except ValueError as ex:
    # we are making sure that we work with values(int) only
    print(f"Errors = {repr(ex)}")

