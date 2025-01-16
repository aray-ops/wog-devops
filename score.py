
from typing import Union
import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

def add_score(difficulty: int) -> Union[int, float]:
    """
    Add winning points to the user's score file.
    Points formula: (difficulty * 3) + 5
    
    Args:
        difficulty (int): The game difficulty level
        
    Returns:
        Union[int, float]: The new score or BAD_RETURN_CODE if failed
    """
    POINTS_OF_WINNING = (difficulty * 3) + 5
    
    try:
        # Read current score or create new file
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as f:
                current_score = float(f.read().strip() or 0)
        else:
            current_score = 0
            
        # Add new points
        new_score = current_score + POINTS_OF_WINNING
        
        # Save updated score
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(new_score))
            
        return new_score
        
    except Exception as e:
        print(f"Error updating score: {str(e)}")
        return BAD_RETURN_CODE
