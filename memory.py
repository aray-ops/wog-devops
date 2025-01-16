import random
import time
from typing import List
from utils import screen_cleaner

def generate_sequence(difficulty: int) -> List[int]:
    """
    Generate a list of random numbers.
    
    Args:
        difficulty (int): Length of the sequence to generate
        
    Returns:
        List[int]: List of random numbers between 1 and 101
    """
    return [random.randint(1, 101) for _ in range(difficulty)]

def display_sequence(sequence: List[int]) -> None:
    """
    Display the sequence to the user for 0.7 seconds.
    
    Args:
        sequence (List[int]): The sequence to display
    """
    print("\nMemorize the following numbers:")
    print(sequence)
    time.sleep(0.7)
    screen_cleaner()

def get_list_from_user(length: int) -> List[int]:
    """
    Get a list of numbers from the user.
    
    Args:
        length (int): Expected length of the list
        
    Returns:
        List[int]: User's input as a list of numbers
    """
    numbers = []
    print(f"\nEnter {length} numbers that you saw:")
    
    for i in range(length):
        while True:
            try:
                num = int(input(f"Number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                
    return numbers

def is_list_equal(list1: List[int], list2: List[int]) -> bool:
    """
    Compare two lists for equality.
    
    Args:
        list1 (List[int]): First list
        list2 (List[int]): Second list
        
    Returns:
        bool: True if lists are identical, False otherwise
    """
    return list1 == list2

def play(difficulty: int) -> bool:
    """
    Run the memory game.
    
    Args:
        difficulty (int): Game difficulty level
        
    Returns:
        bool: True if user wins, False otherwise
    """
    print("\nWelcome to the Memory Game!")
    print("Get ready to memorize some numbers...")
    time.sleep(2)
    
    # Generate and display sequence
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    
    # Get user's guess
    user_sequence = get_list_from_user(difficulty)
    
    # Compare results
    result = is_list_equal(sequence, user_sequence)
    
    if result:
        print("\nCorrect! You remembered all the numbers!")
    else:
        print(f"\nSorry! The correct sequence was: {sequence}")
    
    return result
