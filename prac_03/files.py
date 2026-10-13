# 1.
# user_name = input("Enter your name: ")
# out_file = (open("name.txt", "w"))
#
# out_file.write(user_name)
#
#
# out_file.close()

# 2
# user_name = input("Enter your name: ")
#
# out_file = (open("name.txt", "w"))
# out_file.write(user_name)
# out_file.close()
#
# out_file = open("name.txt", "r")
# print(f"Hi {out_file.read()}!")
# out_file.close()

# 3
# with open("numbers.txt", "r") as file:
#     first_number = int(file.readline())
#     second_number = int(file.readline())
#     result = first_number + second_number
#
# print(result)

# 4
with open("numbers.txt", "r") as file:
    result = 0
    for line in file:
        numbers = int(line)
        result += numbers
    print(result)




