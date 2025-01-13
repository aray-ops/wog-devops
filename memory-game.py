import random
import time
import os

def generate_sequence(difficulty):
    """Generate a list of random numbers between 1 and 101"""
    return [random.randint(1, 101) for _ in range(difficulty)]

def display_sequence(sequence):
    """Display the sequence for 0.7 seconds"""
    print("\nMemorize the following sequence:")
    print(sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')

def get_list_from_user(difficulty):
    """Get sequence of numbers from user"""
    print(f"\nEnter {difficulty} numbers you saw, one at a time:")
    user_sequence = []
    for i in range(difficulty):
        while True:
            try:
                num = input(f"Number {i+1}: ").strip()
                if not num.isdigit():
                    print("Please enter a valid number.")
                    continue
                user_sequence.append(int(num))
                break
            except ValueError:
                print("Please enter a valid number.")
    return user_sequence

def is_list_equal(list1, list2):
    """Compare two lists for equality"""
    return list1 == list2

def play(difficulty):
    """Main game function"""
    sequence = generate_sequence(difficulty)
    display_sequence(sequence)
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_sequence)
