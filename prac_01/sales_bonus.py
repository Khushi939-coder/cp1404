"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sale = float(input("Enter the sale: "))

if sale < 1000:
    bonus = sale * 0.10
else:
    bonus = sale * 0.15

print(f"You get a bonus of ${bonus:.2f}")