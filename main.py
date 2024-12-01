from app import welcome, start_play

def main():
    username = input("Enter your name: ")
    welcome(username)
    start_play()

if __name__ == "__main__":
    main()
