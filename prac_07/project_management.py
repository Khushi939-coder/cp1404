from project import Project

MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

print("Welcome to Pythonic Project Management")

def main():
    projects = load_projects("projects.txt")
    user_input = ""
    while user_input != "Q":
        print(MENU)
        user_input = input(">>> ").upper()
        if user_input == "L":
            filename = input("Enter filename: ")
            load_projects(filename)
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


def load_projects(filename):
    projects = []
    try:
        with open(filename, "r") as file:
            next(file)

            for line in file:
                data = line.strip().split("\t")
                new_project = Project(data[0], (data[1]), int(data[2]), float(data[3]), int(data[4]))
                projects.append(new_project)
    except FileNotFoundError:
        print("File not found.")

    return projects

def save_projects(projects, filename="projects.txt"):
    try:
        with open(filename, "w") as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")

            for p in projects:
                line = f"{p.name}\t{p.date}\t{p.priority}\t{p.cost}\t{p.completion_percentage}\n"
                file.write(line)
        print("Project saved.")
    except Exception as e:
        print(f"Error saving project: {e}")

def display_projects(projects):
    completed = []
    incomplete = []

    # Step 1: Split projects into two groups
    for p in projects:
        if p.completion_percentage == 100:
            completed.append(p)
        else:
            incomplete.append(p)

    # Step 2: Sort both lists (uses the __lt__ method)
    completed.sort()
    incomplete.sort()

    # Step 3: Print them
    print("\n--- Incomplete Projects ---")
    for p in incomplete:
        print(p)

    print("\n--- Completed Projects ---")
    for p in completed:
        print(p)





def filter_projects_by_date():
    pass

def add_new_project():
    pass

def update_project():
    pass

if __name__ == "__main__":
    main()