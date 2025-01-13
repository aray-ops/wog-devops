from utils import SCORES_FILE_NAME

def calculate_points(difficulty):
    """Calculate points based on difficulty"""
    return (difficulty * 3) + 5

def add_score(difficulty):
    """Add score to scores file"""
    points = calculate_points(difficulty)
    
    try:
        # Try to read current score
        with open(SCORES_FILE_NAME, 'r') as f:
            current_score = int(f.read().strip() or 0)
    except (FileNotFoundError, ValueError):
        current_score = 0
    
    # Add new points
    new_score = current_score + points
    
    # Write updated score
    try:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(new_score))
        return True
    except Exception as e:
        print(f"Error saving score: {e}")
        return False
