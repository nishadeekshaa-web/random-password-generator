import random
import string

def generate_random_password(length=12):
    """
    Generates a random password of a specified length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password_list = []
    for _ in range(length):
        random_char = random.choice(characters)
        password_list.append(random_char)
    random.shuffle(password_list)
    password = "".join(password_list)
    return password
try:
    password_length = int(input("Enter the desired password length (default is 12): ") or 12)
except ValueError:
    print("Invalid input. Using default length of 12.")
    password_length = 12
new_password = generate_random_password(password_length)
print(f"Generated Password: {new_password}")