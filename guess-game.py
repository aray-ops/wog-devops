import random

def generate_number(difficulty):
    """Generate a random number between 0 and difficulty"""
    return random.randint(0, difficulty)  # Changed to start from 0

def get_guess_from_user(difficulty):
    """Get user's guess between 0 and difficulty"""
    while True:
        try:
            guess = input(f"Please guess a number between 0 and {difficulty}: ").strip()  # Changed message
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            guess = int(guess)
            if 0 <= guess <= difficulty:  # Changed range check
                return guess
            print(f"Number must be between 0 and {difficulty}.")
        except ValueError:
            print("Please enter a valid number.")

def compare_results(secret_number, guess):
    """Compare the secret number with user's guess"""
    return secret_number == guess

def play(difficulty):
    """Main game function"""
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)