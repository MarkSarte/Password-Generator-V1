#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the #Mark's Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Initializes a variable string to be used in a for loop
password_characters = ""

#Randomizes the characters based on how many characters the user wants and concatenate it.
for i in range(0, nr_letters):
    letter_picker = random.choice(letters)
    password_characters += letter_picker
for i in range(0, nr_numbers):
    number_picker = random.choice(numbers)
    password_characters += number_picker
for i in range(0, nr_symbols):
    symbol_picker = random.choice(symbols)
    password_characters += symbol_picker

#Converts the concatenated characters in to list
password_list = list(password_characters)
#Randomizes the characters in the list and convert it back to a string
random.shuffle(password_list)
password = ''.join(password_list)

print(password)