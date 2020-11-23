#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised: **DO NOT USE = unless using random shuffle *********
# password = ""
# # nr_letters = 4
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
2
# print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):  # 12
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):  # 4
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):  # 4
    password_list += random.choice(numbers)

print(password_list)  # ['X', 'b', 'H', 't', 'N', 'S', 'y', 'Z', 'Y', 'b', 'm', 'v', '%', '+', '&', '0', '9', '9', '5']
random.shuffle(password_list)  # ['+', '9', '0', 'H', 'Y', 'N', 'b', 'Z', '&', '9', 'm', 'v', 'S', 'y', 'b', 't', 'X', '5', '%']
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")  # Your password is: +90HYNbZ&9mvSybtX5%
