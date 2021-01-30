username = input("Enter your username = ")
password = input("Enter your password = ")
password_length = len(password)
secret_password = "*" * password_length

print(f"Hey {username}, your password {secret_password} is {password_length} letters long")