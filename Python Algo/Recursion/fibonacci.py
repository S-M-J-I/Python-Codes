# Recursion - Fibonacci

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


n = int(input("Enter n = "))
res = fibo(n)
print(f"Fibonacci of {n} = {res}")
