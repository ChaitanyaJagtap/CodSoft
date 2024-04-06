import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine all character sets based on complexity level
    all_chars = lower_case + upper_case + digits + special_chars

    # Generate password using random.choices
    password = ''.join(random.choices(all_chars, k=length))
    return password

def main():
    try:
        # Prompt the user to specify the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
