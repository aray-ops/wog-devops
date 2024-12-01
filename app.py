def welcome(username):
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def start_play():
    print("Please choose a game to play:")
    print("1. Memory Game - A sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - Guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - Try and guess the value of a random amount of USD in ILS")

    game_choice = int(input("Enter the number of the game you want to play: "))

    if game_choice not in [1, 2, 3]:
        print("Invalid choice, please choose a valid game.")
        return

    difficulty = int(input("Select difficulty level (1 to 5): "))
    if difficulty < 1 or difficulty > 5:
        print("Invalid difficulty level. Please select a level between 1 and 5.")
        return

    if game_choice == 1:
        memory_game(difficulty)
    elif game_choice == 2:
        guess_game(difficulty)
    elif game_choice == 3:
        currency_roulette(difficulty)

def memory_game(difficulty):
        print(f"Starting Memory Game with difficulty {difficulty}...")

def guess_game(difficulty):
        print(f"Starting Guess Game with difficulty {difficulty}...")

def currency_roulette(difficulty):
        print(f"Starting Currency Roulette with difficulty {difficulty}...")