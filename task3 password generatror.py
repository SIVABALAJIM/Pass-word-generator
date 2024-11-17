import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    # Prompt user for password length
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length must be a positive number!")
            return
        
        # Define character sets for password generation
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Combine all character sets
        all_characters = lower + upper + digits + symbols
        
        # Generate a random password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the length.")

generate_password()
