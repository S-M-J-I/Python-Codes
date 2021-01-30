# Recursion - GCD

def GCD(x, y):
    while y > 0:
        rem = x % y
        x = y
        y = rem
    return x


a = int(input("Enter a value = "))
b = int(input("Enter another value = "))
gcd = GCD(a, b)
print(f"GCD of {a} and {b} = {gcd}")
