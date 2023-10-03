import re
import string
import random

def password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 to 15 characters long."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    special_characters = string.punctuation
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."
    
    common_passwords = ["password", "123456", "123456789", "qwerty", "12345", "12345678"]
    if password.lower() in common_passwords:
        return "Password is too common. Please choose a different password."
    
    for char in set(password):
        if password.count(char) > 2:
            return "Password should not have more than two identical characters or digits in a row."
    
    return "Password is strong."

def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    while True:
        password = input("Enter the password: ").strip()  # strip leading/trailing whitespace
        print(password_strength(password))
        
        user_input = input("Would you like to generate a strong password? (yes/no): ").strip().lower()  # sanitize input
        if user_input == 'yes':
            while True:
                generated_password = generate_password()
                print(f"Generated Password: {generated_password}")
                user_input = input("Would you like to regenerate the password? (yes/no): ").strip().lower()  # sanitize input
                if user_input != 'yes':
                    break
        
        user_input = input("Would you like to try again with a new password? (yes/no): ").strip().lower()  # sanitize input
        if user_input != 'yes':
            print("Exiting the program.")
            break
