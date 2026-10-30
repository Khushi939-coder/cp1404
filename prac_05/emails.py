email_to_name = {}

while True:
    user_email = input("Enter email: ")
    if user_email == "":
        break


    # 1. The "Guessing" Recipe
    first_part = user_email.split("@")[0]
    name_parts = first_part.split(".")
    guessed_name = " ".join(name_parts).title()

    # 2. Confirming the name

    confirmation = input(f"Is your name {guessed_name}? (Y/n) ")

    if confirmation == "" or confirmation.lower() == "y":
        final_name = guessed_name
    else:
        final_name = input("Name:")

    # Sorting in the dictionary
    email_to_name[user_email] = final_name

# 4. Print final result
print("--- DEBUG: REACHED THE END ---")
for email, name in email_to_name.items():
    print(f"{name} ({email})")








