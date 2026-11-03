from prac_06.guitar import Guitar

guitar_list = []
print("My guitars!")
user_name = input("Name: ")

while user_name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(user_name, year, cost)
    guitar_list.append(new_guitar)
    print(f"{new_guitar.name} ({new_guitar.year}) : ${new_guitar.cost:,.2f}) added")
    print()
    user_name = input("Name: ")

print("... snip ...")

print("\nThese are my guitars: ")
for i, guitar in enumerate(guitar_list, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")