import os
import platform

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner() -> None:
    """
    Clear the console screen based on the operating system.
    """
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')
