"""Pypassword generator"""

import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'", "<", ">", ",", ".", "/", "?"]
numbers = [0,1,2,3,4,5,6,7,8,9]

print("Welcome to Pypassword generator")
nr_letters = int(input("How many letters would you like to have in your password?\n"))
nr_symbols = int(input("How many symbols would you like to have in your password?\n"))
nr_numbers = int(input("How many numbers would you like to have in your password?\n"))

# # type - 1
# random_letters = random.choices(letters,k=nr_letters)
# random_characters = random.choices(symbols,k=nr_symbols)
# random_numbers = random.choices(numbers,k=nr_numbers)
# password_list = [str(item) for item in random_letters+random_numbers+random_characters]
# random.shuffle(password_list)
# password = ""
# for item in password_list:
#     password += item
# print(f"Your password is: {password}")



# # type - 2
# password_str = ""
# for letter in range(0, nr_letters):
#     password_str += random.choice(letters)
# for symbol in range(0, nr_symbols):
#     password_str += random.choice(symbols)
# for number in range(0, nr_numbers):
#     password_str += random.choice(str(numbers))
# print(f"Your password is: {password_str.strip()}")



# type - 3
password_list = []
for _ in range(0, nr_letters):
    password_list.append(random.choice(letters))
for _ in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for char in password_list:
    password += str(char)

print(f"Your password is: {password}")
