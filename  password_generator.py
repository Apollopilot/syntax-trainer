# password_generator.py
import string
import random
letters = string.ascii_letters
digits = string.digits
symbols = "!@#$%^&*()"

all_chars = letters + digits + symbols 

length = int(input( "Enter Password Length "))

password = ''.join(random.choices(all_chars, k=length))

print("Generated password: ", password) 