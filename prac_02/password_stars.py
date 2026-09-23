PASSWORD = "******"

def main():
    """Password checker"""
    print("Welcome to password checker")
    password = input("Enter your password: ")

    while not is_valid(password):
        print("Passwords do not match")
        password = input("Enter your password: ")

    print("Access granted!")

def is_valid(password):
    """Check if password is valid"""
    return password == PASSWORD

main()




