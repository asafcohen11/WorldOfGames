import GuessGame, MemoryGame, CurrencyRouletteGame, Score


def welcome(name):
    msg = f"""Hello {name} and welcome to the World Of Games (WoG).
    Here you can find many cool games to play"""
    return msg


def load_game():
    msg = """Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to 
    guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS 
    """
    game = int(input(msg))

    if game < 1 or game > 3:
        input("Invalid option! Valid options are 1, 2 or 3. \nClick any key to exit.")
        exit(1)

    difficulty = int(input("Please choose game difficulty from 1 to 5:"))

    if difficulty < 1 or difficulty > 5:
        input("Invalid option! Should be 1 to 5. \nClick any key to exit.")
        exit(2)

    if game == 1:
        if MemoryGame.play(difficulty):
            Score.add_score(difficulty)
            print("You won the Game!")
        else:
            print("You lost the Game")
    elif game == 2:
        if GuessGame.play(difficulty):
            Score.add_score(difficulty)
            print("You won the Game!")
        else:
            print("You lost the Game")
    elif game == 3:
        if CurrencyRouletteGame.play(difficulty):
            Score.add_score(difficulty)


