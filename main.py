#Fairus De La Cruz Random Password Generator


'''''
A function for password
like how long it should be
letters in lower and uppercase
numbers and special characters
'''''
import random
import string

# Function to see how long the user wants the password to be
def first_step():
    how_long = int(input('How long is your password? '))
    return how_long

# Function to see if the user wants letters in their password
def letters():
    upper_letters = input("Does it need uppercase letters? (yes/no) ").strip().lower() == 'yes'
    lower_letters = input("Does it need lowercase letters? (yes/no) ").strip().lower() == 'yes'
    return upper_letters, lower_letters

# Function to ask the user if they want to use special characters
def special_characters():
    special_characters = input("Do you want special characters? (yes/no) ").strip().lower() == 'yes'
    return special_characters

# Function to ask the user if they want to use numbers
def numbers():
    numbers = input("Do you want numbers? (yes/no) ").strip().lower() == 'yes'
    return numbers

# Function to generate the password
def generate_password(how_long, upper_letters, lower_letters, special_characters, numbers):
    all_characters = ''
    if upper_letters:
        all_characters += string.ascii_uppercase
    if lower_letters:
        all_characters += string.ascii_lowercase
    if special_characters:
        all_characters += string.punctuation
    if numbers:
        all_characters += string.digits

    if not all_characters:
        return None

    password = ''.join(random.choice(all_characters) for _ in range(how_long))
    return password

# Fully run the code
def main():
    how_long = first_step()
    upper_letters, lower_letters = letters()
    special_characters_flag = special_characters()
    numbers_flag = numbers()

    password_list = []
    while len(password_list) < 4:
        password = generate_password(how_long, upper_letters, lower_letters, special_characters_flag, numbers_flag)
        if password:
            password_list.append(password)

    print("\nGenerated Passwords:")
    for password in password_list:
        print(password)

if __name__ == "__main__":
    main()
