import games


def welcome(name) -> None:
    print(f"Hello {name} and welcome to the World of games (WoG)")
    print("Here you can find many cool games to play")


def load_game() -> None:
    print("Please chose a game to play:")
    game_dict = {1: "Memory Game",
                 2: "Guess Game",
                 3: "Currency Game"}
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game_number = input(f"\n")
    while True:
        if game_number.isdigit():
            game_number = int(game_number)
            if game_number in game_dict:
                game_name = game_dict[game_number]
                print(f"you chose {game_name}")
                break

            game_number = input("Please enter a valid game number (1-3)\n")
        else:
            game_number = input("Please enter a valid game number (1-3)\n")
    user_difficulty = input("Please choose difficulty level between 1-5\n")
    while True:
        if user_difficulty.isdigit():
            user_difficulty = int(user_difficulty)
            if 0 < user_difficulty <= 5:
                print(f"you chose {game_name} in difficulty {user_difficulty}")
                break

            user_difficulty = input("Please enter a valid difficulty value (1-5)\n")
        else:
            user_difficulty = input("Please enter a valid difficulty value (1-5)\n")
