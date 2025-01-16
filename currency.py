import random
from typing import Tuple
import requests
from typing import Optional

def get_current_exchange_rate() -> float:
    """
    Get the current USD to ILS exchange rate using a free API.
    
    Returns:
        float: Current exchange rate
    """
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        return data['rates']['ILS']
    except Exception as e:
        print(f"Error fetching exchange rate: {str(e)}")
        # Fallback to approximate rate if API fails
        return 3.6

def get_money_interval(difficulty: int) -> Tuple[float, float]:
    """
    Calculate the interval for a correct guess based on difficulty.
    
    Args:
        difficulty (int): Game difficulty level
        
    Returns:
        Tuple[float, float]: Lower and upper bounds for correct guess
    """
    # Generate random amount between 1-100 USD
    usd_amount = random.randint(1, 100)
    # Get current exchange rate
    rate = get_current_exchange_rate()
    # Calculate exact value in ILS
    ils_value = usd_amount * rate
    # Calculate interval based on difficulty
    interval = 10 - difficulty
    
    return ils_value - interval, ils_value + interval, usd_amount

def get_guess_from_user(usd_amount: int) -> Optional[float]:
    """
    Get user's guess for the ILS value.
    
    Args:
        usd_amount (int): The amount in USD to convert
        
    Returns:
        Optional[float]: User's guess or None if invalid
    """
    while True:
        try:
            print(f"\nHow much is ${usd_amount} in ILS?")
            guess = float(input("Your guess: "))
            if guess > 0:
                return guess
            print("Please enter a positive number")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def play(difficulty: int) -> bool:
    """
    Run the currency roulette game.
    
    Args:
        difficulty (int): Game difficulty level
        
    Returns:
        bool: True if user wins, False otherwise
    """
    print("\nWelcome to the Currency Roulette Game!")
    print("Try to guess the value in ILS...")
    
    # Get interval and USD amount
    lower_bound, upper_bound, usd_amount = get_money_interval(difficulty)
    
    # Get user's guess
    guess = get_guess_from_user(usd_amount)
    if guess is None:
        return False
    
    # Check if guess is within interval
    is_correct = lower_bound <= guess <= upper_bound
    
    if is_correct:
        print(f"\nCorrect! ${usd_amount} is between {lower_bound:.2f} and {upper_bound:.2f} ILS")
    else:
        print(f"\nSorry! ${usd_amount} is between {lower_bound:.2f} and {upper_bound:.2f} ILS")
    
    return is_correct
