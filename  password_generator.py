# password_generator.py
import string
import random
letters = string.ascii_letters # shortcut that returns a string containing a-z, A-Z
digits = string.digits # shortcut that returns string containing 1-9
symbols = "!@#$%^&*()"

while True: #infinite loop
    length = int(input( "Enter Password Length (minimum 3): ")) #integer to string with input

    if length < 3:
        print("Password must be at least 3 characters long ") #sends back to beginning of loop
        
    if length == "done":
        exit 
    else: 
        break #exits loop if valid

    
password_chars = [
     random.choice(letters),
     random.choice(digits),
     random.choice(symbols)   
    ]
all_chars = letters + digits + symbols # concatenation 
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