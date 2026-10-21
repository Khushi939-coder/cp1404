numbers = []
for i in range(5):
    user_input = int(input("Number: "))
    numbers.append(user_input)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[4]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {sum(numbers)/len(numbers)}")

