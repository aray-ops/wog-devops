import os

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    """Clear the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
