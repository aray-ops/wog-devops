class GameApp:
    def __init__(self):
        self.username = ""
        self.games = {
            1: {
                "name": "Memory Game",
                "function": self.memory_game,
                "description": "A sequence of numbers will appear for 1 second and you have to guess it back."
            },
            2: {
                "name": "Guess Game",
                "function": self.guess_game,
                "description": "Guess a number and see if you chose like the computer."
            },
            3: {
                "name": "Currency Roulette",
                "function": self.currency_roulette,
                "description": "Try and guess the value of a random amount of USD in ILS"
            }
        }

    def start(self):
        self.get_username()
        self.welcome()
        self.start_play()

    def get_username(self):
        while True:
            self.username = input("Enter your name: ").strip()
            if self.username and self.username.replace(" ", "").isalpha():
                break
            print("Username must contain only letters and spaces and cannot be empty.")

    def welcome(self):
        print(f"Hi {self.username} and welcome to the World of Games: The Epic Journey")

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            user_input = input(prompt).strip()
            
            # Check if input is a digit first
            if not user_input.isdigit():
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")
                continue
            
            # Convert to integer after validation
            value = int(user_input)
            
            # Check range
            if min_val <= value <= max_val:
                return value
            
            print(f"Please enter a number between {min_val} and {max_val}.")

    def start_play(self):
        print("\nPlease choose a game to play:")
        for num, game_info in self.games.items():
            print(f"{num}. {game_info['name']}")
            print(f"   {game_info['description']}")

        game_choice = self.get_valid_input(
            "Enter the number of the game you want to play: ", 
            1, 
            len(self.games)
        )
        
        difficulty = self.get_valid_input(
            "Select difficulty level (1 to 5): ",
            1,
            5
        )
        
        # Execute the chosen game with selected difficulty
        self.games[game_choice]["function"](difficulty)

    def memory_game(self, difficulty):
        print(f"Starting Memory Game with difficulty {difficulty}...")

    def guess_game(self, difficulty):
        print(f"Starting Guess Game with difficulty {difficulty}...")

    def currency_roulette(self, difficulty):
        print(f"Starting Currency Roulette with difficulty {difficulty}...")
