# Import necessary libraries
import random
import string

# Get user input for the desired length of the password
length = int(input("Enter the length of the password: "))

# Define a function to generate a random password
def generate_password(length):
    # Define special characters that can be included in the password
    special_characters = "!@#$%&"
    
    # Generate a random password using lowercase letters, digits, and special characters
    password = ''.join(random.choices(string.ascii_lowercase + string.digits + special_characters, k=length))
    
    # Print the generated password
    print(password)

# Call the generate_password function with the specified length
generate_password(length)
