"""
Password Generator
-------------------
A simple command-line tool that generates strong, random passwords.
"""

import random
import string


def get_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_complexity_options():
    print("\nChoose the complexity of your password.")
    print("Answer y/n for each option:")

    use_lower = input("Include lowercase letters (a-z)? (y/n): ").strip().lower() == "y"
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").strip().lower() == "y"
    use_digits = input("Include digits (0-9)? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include special characters (!@#$...)? (y/n): ").strip().lower() == "y"

    if not any([use_lower, use_upper, use_digits, use_symbols]):
        print("\nNo options selected. Defaulting to letters + digits.")
        use_lower = use_upper = use_digits = True

    return use_lower, use_upper, use_digits, use_symbols


def build_character_pool(use_lower, use_upper, use_digits, use_symbols):
    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return pool


def generate_password(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def main():
    print("=== Random Password Generator ===\n")

    length = get_length()
    use_lower, use_upper, use_digits, use_symbols = get_complexity_options()
    pool = build_character_pool(use_lower, use_upper, use_digits, use_symbols)

    password = generate_password(length, pool)

    print("\nYour generated password is:")
    print(password)


if __name__ == "__main__":
    main()