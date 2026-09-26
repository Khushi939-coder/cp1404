"""
CP1404/CP5632 - Practical
Program to determine score status
"""

# score = float(input("Enter score: "))
# if score < 0 or score > 100:
#     print("Invalid score")
# elif score >= 90:
#     print("Excellent")
# elif score >= 50:
#     print("Passable")
# else:
#     print("Bad")

import random

def main():
    """Main function to ask for score and print result"""
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        result = score_result(score)
        print(f"User score {score} is {result}")

        if result == "Excellent":
            print("You get a prize!")

    random_score = random.randint(0, 100)
    result = score_result(random_score)
    print(f"Random: {random_score} = {result}")


def score_result(score):
    """Return score status for user"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()