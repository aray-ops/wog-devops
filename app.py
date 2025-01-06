class GameApp:
    def __init__(self):
        self.username = ""
        self.games = {
            1: ("Memory Game", self.memory_game),
            2: ("Guess Game", self.guess_game),
            3: ("Currency Roulette", self.currency_roulette)
        }

    def start(self):
        self.get_username()
        self.welcome()
        self.start_play()

    def get_username(self):
        self.username = input("Enter your name: ").strip()
        while not self.username:
            print("Username cannot be empty.")
            self.username = input("Enter your name: ").strip()

    def welcome(self):
        print(f"Hi {self.username} and welcome to the World of Games: The Epic Journey")

    def get_valid_input(self, prompt, min_val, max_val, input_type=int):
        while True:
            try:
                value = input_type(input(prompt))
                if min_val <= value <= max_val:
                    return value
                print(f"Please enter a number between {min_val} and {max_val}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between {min_val} and {max_val}.")

    def start_play(self):
        print("Please choose a game to play:")
        for num, (game_name, _) in self.games.items():
            print(f"{num}. {game_name}")
            if num == 1:
                print("   A sequence of numbers will appear for 1 second and you have to guess it back.")
            elif num == 2:
                print("   Guess a number and see if you chose like the computer.")
            elif num == 3:
                print("   Try and guess the value of a random amount of USD in ILS")

        game_choice = self.get_valid_input("Enter the number of the game you want to play: ", 1, 3)
        difficulty = self.get_valid_input("Select difficulty level (1 to 5): ", 1, 5)
        
        self.games[game_choice][1](difficulty)

    def memory_game(self, difficulty):
        print(f"Starting Memory Game with difficulty {difficulty}...")

    def guess_game(self, difficulty):
        print(f"Starting Guess Game with difficulty {difficulty}...")

    def currency_roulette(self, difficulty):
        print(f"Starting Currency Roulette with difficulty {difficulty}...")
