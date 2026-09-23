PASSWORD = "******"

def main():
    """Password checker"""
    print("Welcome to the password checker!")

    password = input("Enter your password: ")

    while password != PASSWORD:
        print("Incorrect password")
        password = input("Enter your password: ")

    print("Access granted!")

def is_valid(password):
    """Check if password is valid"""
    return password == PASSWORD

if __name__ == "__main__":
    main()