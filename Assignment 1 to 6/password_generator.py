import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# CLI Input
print("Password Generator by Maria Khan")

while True:
    try:
        length = int(input("Enter password length (6-32): "))
        if 6 <= length <= 32:
            break
        else:
            print("Please enter a number between 6 and 32.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

# Generate Password
password = generate_password(length, use_digits, use_special)
print(f"\nGenerated Password: {password}")
