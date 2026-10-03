MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    """Main function to handle menu"""
    score = valid_score()

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = valid_score()
        elif choice == "P":
            print(f"Result: {score_result(score)}")
        elif choice == "S":
            print(f"The stars are {show_stars(score)}")
        else:
            print(f"Invalid choice: {choice}")
        choice = input(">>> ").upper()

    print("Farewell")

def valid_score():
    """Function to validate score"""
    while True:
        try:
            score = int(input("Enter score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Score must be an integer")

def score_result(score):
    """Return score status for user"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Show stars as many as score"""
    stars = "*" * score
    return stars

if __name__ == '__main__':
    main()


