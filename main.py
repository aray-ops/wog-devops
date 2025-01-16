from app import welcome, start_play

def main():
    """
    Main entry point for the World of Games application.
    """
    name = input("Please enter your name: ")
    print(welcome(name))
    start_play()

if __name__ == "__main__":
    main()
