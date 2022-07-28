#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_charachters = []

# Choose random letters
for iteration in range(nr_letters):
    rnd_letter_choice = random.randint(0, len(letters) - 1)
    password_charachters.append(letters[rnd_letter_choice])

# Choose random symbols
for iteration in range(nr_symbols):
    rnd_symbol_choice = random.randint(0, len(symbols) - 1)
    password_charachters.append(symbols[rnd_symbol_choice])

# Choose random numbers
for iteration in range(nr_numbers):
    rnd_number_choice = random.randint(0, len(numbers) - 1)
    password_charachters.append(numbers[rnd_number_choice])

# Shuffle password charachters
random.shuffle(password_charachters)

# Output password
password = ''.join(password_charachters)

print("Your password is:", password)