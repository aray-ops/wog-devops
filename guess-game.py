import random

def generate_number(difficulty):
    """Generate a random number between 1 and difficulty"""
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty):
    """Get user's guess between 1 and difficulty"""
    while True:
        try:
            guess = input(f"Please guess a number between 1 and {difficulty}: ").strip()
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue
            guess = int(guess)
            if 1 <= guess <= difficulty:
                return guess
            print(f"Number must be between 1 and {difficulty}.")
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
