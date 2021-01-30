# Recursion - Factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter n = "))
fact = factorial(n)
print(f"Factorial of {n} = {fact}")
