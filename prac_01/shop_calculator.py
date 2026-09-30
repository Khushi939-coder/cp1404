total_price = 0
number_of_items = int(input("Enter the number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Enter the number of items: "))

for i in range(0, number_of_items, 1):
    price = float(input("Enter the price: "))
    total_price += price

if total_price > 100:
    final_price = total_price * 0.90
else:
    final_price = total_price
print(f"The total price for {number_of_items} items is ${final_price:.2f} ")