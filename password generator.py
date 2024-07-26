import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    allowed_characters = ""
    if use_upper:
        allowed_characters += uppercase_letters
    if use_lower:
        allowed_characters += lowercase_letters
    if use_digits:
        allowed_characters += digits
    if use_special:
        allowed_characters += special_characters

    password = "".join(random.choice(allowed_characters) for _ in range(length))
    return password

def main():
    try:
        desired_length = int(input("Enter desired password length: "))
        password = generate_password(length=desired_length)

        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
