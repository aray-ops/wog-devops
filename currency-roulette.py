import random
from forex_python.converter import CurrencyRates

def get_money_interval(difficulty, usd_amount):
    """Calculate the interval for correct guess based on difficulty"""
    try:
        c = CurrencyRates()
        # Get the current exchange rate from USD to ILS
        usd_to_ils_rate = c.get_rate('USD', 'ILS')
        # Calculate the exact value in ILS
        exact_value = usd_amount * usd_to_ils_rate
        # Calculate interval based on difficulty
        interval = 10 - difficulty
        return exact_value - interval, exact_value + interval
    except Exception as e:
        print(f"Error getting exchange rate: {e}")
        return None, None

def get_guess_from_user(usd_amount):
    """Get user's guess for the value in ILS"""
    while True:
        try:
            guess = input(f"How much is ${usd_amount} in ILS? ").strip()
            if not guess.replace('.', '').isdigit():
                print("Please enter a valid number.")
                continue
            return float(guess)
        except ValueError:
            print("Please enter a valid number.")

def play(difficulty):
    """Main game function"""
    # Generate random USD amount between 1-100
    usd_amount = random.randint(1, 100)
    
    # Get interval
    lower_bound, upper_bound = get_money_interval(difficulty, usd_amount)
    if lower_bound is None:
        return False
    
    # Get user's guess
    user_guess = get_guess_from_user(usd_amount)
    
    # Check if guess is within interval
    return lower_bound <= user_guess <= upper_bound
