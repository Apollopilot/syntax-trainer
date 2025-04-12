# password_generator.py
import string
import random
letters = string.ascii_letters # shortcut that returns a string containing a-z, A-Z
digits = string.digits # shortcut that returns string containing 1-9
symbols = "!@#$%^&*()"
all_chars = letters + digits + symbols # concatenation 

while True: #infinite loop
    user_input = input("Enter password length (min 3) or type 'done' to quit: ")

    if user_input.lower() == 'done':
        print("Douces !")
        break

    if not user_input.isdigit():
        print("Please enter a number or type 'done'.")
        continue

    length = int(user_input)

    if length < 3:
        print("Quit being an idiot...at least 3 characters")
        continue 

    
    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)   
    ]

    password_chars = random.choices(all_chars, k=length - 3) #string joining

    random.shuffle(password_chars) #shuffle to make it unpredictable

    password = ''.join(password_chars)

    print("Secured password: ", password) 

## summary of concepts used

# Module import
# User input 
# Type conversion ('int()')
# Random selections ('random.choices(population, k=number)') function does 2 things What to choose from and how many things to choose (called k)
# String joining (' ''.join()')
# Variables, concatenation, function calls