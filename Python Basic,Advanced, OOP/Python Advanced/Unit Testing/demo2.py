import random

# exercise - do unit testing on this piece of code
# when testing,it is better to have code within functions

def run_guess(guesses, answers):
    try:
        if 0 < guesses < 11:
            if guesses == answers:
                print('you are a genius!')
                return True
        else:
            print('hey bozo, I said 1~10')
            return False
    except ValueError as ex:
        print("Please enter a number")
        return ex


if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        guess = int(input('guess a number 1~10:  '))
        if run_guess(guess, answer):
            break
