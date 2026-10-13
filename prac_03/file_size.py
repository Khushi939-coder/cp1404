def main():
    user_input = input("Enter filename: ")
    while user_input != "":
        try:
            print(f"{user_input} has {count_lines(user_input)} lines")
        except FileNotFoundError:
            print(f"ERROR: {user_input} does not exist.")

        user_input = input("Enter filename: ")


def count_lines(filename):
    count = 0
    with open(filename, "r") as file:
     for line in file:
        count += 1
     return count


main()




