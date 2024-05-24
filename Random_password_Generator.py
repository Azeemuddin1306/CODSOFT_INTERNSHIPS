import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt user for password length
    length = int(input("Enter the length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
