import random
from typing import Optional

def generate_number(difficulty: int) -> int:
    """
    Generate a random number between 1 and difficulty.
    
    Args:
        difficulty (int): The upper bound for the random number
        
    Returns:
        int: The generated secret number
    """
    return random.randint(1, difficulty)

def get_guess_from_user(difficulty: int) -> Optional[int]:
    """
    Get the user's guess between 1 and difficulty.
    
    Args:
        difficulty (int): The upper bound for valid guesses
        
    Returns:
        Optional[int]: The user's valid guess or None if invalid
    """
    while True:
        try:
            guess = input(f"\nPlease guess a number between 1 and {difficulty}: ")
            guess_num = int(guess)
            if 1 <= guess_num <= difficulty:
                return guess_num
            print(f"Please enter a number between 1 and {difficulty}")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        
def compare_results(secret_number: int, guess: int) -> bool:
    """
    Compare the secret number with the user's guess.
    
    Args:
        secret_number (int): The generated secret number
        guess (int): The user's guess
        
    Returns:
        bool: True if the numbers match, False otherwise
    """
    return secret_number == guess

def play(difficulty: int) -> bool:
    """
    Run the guess game.
    
    Args:
        difficulty (int): The game difficulty level
        
    Returns:
        bool: True if user wins, False otherwise
    """
    print("\nWelcome to the Guess Game!")
    print(f"I'm thinking of a number between 1 and {difficulty}")
    
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    
    if guess is None:
        return False
        
    return compare_results(secret_number, guess)
