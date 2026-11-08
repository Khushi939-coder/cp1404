MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

print("Welcome to Pythonic Project Management")

def main():
    user_input = ""
    while user_input != "Q":
        print(MENU)
        user_input = input(">>> ").upper()
        if user_input == "L":
            load_projects()
        elif user_input == "S":
            save_projects()
        elif user_input == "D":
            display_projects()
        elif user_input == "F":
            filter_projects_by_date()
        elif user_input == "A":
            add_new_project()
        elif user_input == "U":
            update_project()
        else:
            print("Invalid input. Try again.")


def load_projects():
    pass

def save_projects():
    pass

def display_projects():
    pass

def filter_projects_by_date():
    pass

def add_new_project():
    pass

def update_project():
    pass

if __name__ == "__main__":
    main()