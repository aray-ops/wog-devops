from typing import Tuple, Optional
import os
from memory import play as memory_game_play
from guess import play as guess_game_play
from currency import play as currency_game_play
from utils import screen_cleaner, SCORES_FILE_NAME
from score import add_score

def welcome(name: str) -> str:
    """
    Display a welcome message to the user.
    
    Args:
        name (str): The user's name
        
    Returns:
        str: Formatted welcome message
    """
    return f"Hi {name} and welcome to the World of Games: The Epic Journey"

def _validate_input(user_input: str, min_val: int, max_val: int) -> Optional[int]:
    """
    Validate user input is a number within the specified range.
    
    Args:
        user_input (str): The user's input string
        min_val (int): Minimum acceptable value
        max_val (int): Maximum acceptable value
        
    Returns:
        Optional[int]: Valid integer if input is valid, None otherwise
    """
    try:
        value = int(user_input)
        if min_val <= value <= max_val:
            return value
        return None
    except ValueError:
        return None

def get_game_choice() -> Optional[int]:
    """
    Present game options and get valid user choice.
    
    Returns:
        Optional[int]: Valid game choice (1-3) or None if user wants to quit
    """
    while True:
        print("\nPlease choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
        print("q. Quit")
        
        choice = input("\nYour choice: ").lower()
        if choice == 'q':
            return None
            
        valid_choice = _validate_input(choice, 1, 3)
        if valid_choice:
            return valid_choice
            
        print("\nInvalid input! Please enter a number between 1 and 3, or 'q' to quit.")

def get_game_difficulty() -> Optional[int]:
    """
    Get valid difficulty level from user.
    
    Returns:
        Optional[int]: Valid difficulty (1-5) or None if user wants to quit
    """
    while True:
        print("\nPlease choose game difficulty from 1 to 5:")
        print("1 = Easy, 5 = Hard")
        print("q = Quit")
        
        difficulty = input("\nYour choice: ").lower()
        if difficulty == 'q':
            return None
            
        valid_difficulty = _validate_input(difficulty, 1, 5)
        if valid_difficulty:
            return valid_difficulty
            
        print("\nInvalid input! Please enter a number between 1 and 5, or 'q' to quit.")

def start_play() -> None:
    """
    Main game loop that handles game selection, difficulty setting, and score management.
    """
    while True:
        screen_cleaner()
        game_choice = get_game_choice()
        if not game_choice:
            print("\nThanks for playing! Goodbye!")
            break
            
        difficulty = get_game_difficulty()
        if not difficulty:
            continue
            
        # Map game choice to corresponding play function
        game_functions = {
            1: memory_game_play,
            2: guess_game_play,
            3: currency_game_play
        }
        
        game_function = game_functions.get(game_choice)
        if game_function:
            try:
                won = game_function(difficulty)
                if won:
                    add_score(difficulty)
                    print("\nCongratulations! You won!")
                else:
                    print("\nBetter luck next time!")
            except Exception as e:
                print(f"\nAn error occurred while playing the game: {str(e)}")
                continue
                
        play_again = input("\nWould you like to play another game? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break
