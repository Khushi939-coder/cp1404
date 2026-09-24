"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print(f"Result: {fahrenheit:.2f} F")
#     elif choice == "F":
#         fahrenheit = float(input("Fahrenheit : "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print(f"Result: {celsius:.2f} C")
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
print(MENU)

def main():
    """Main function to handle menu and conversions"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature: {convert_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature: {convert_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid input")

        print(MENU)
        choice = input(">>> ").upper()

def convert_to_fahrenheit(celsius):
    """Convert user input into Fahrenheit"""
    return celsius * 9.0 / 5 + 32

def convert_to_celsius(fahrenheit):
    """Convert user input into Celsius"""
    return 5 / 9 * (fahrenheit - 32)


main()