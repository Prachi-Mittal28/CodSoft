import random
import string

def generate_password(length):
    if length <= 0:
        return "Error: Password length must be greater than 0."

    # Define the character sets to use in the password
    upper_letters = string.ascii_uppercase
    lower_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets into one pool
    all_characters = upper_letters + lower_letters + digits + special_characters
    
    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
            
            next_step = input("Do you want to generate another password? (yes/no): ")
            if next_step.lower() != 'yes':
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
