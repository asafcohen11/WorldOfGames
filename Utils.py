import os

"""A general purpose python file. This file will contain general information and operations we need
for our game.
1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
2. BAD_RETURN_CODE - A number representing a bad return code for a function.
3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts)."""

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')


screen_cleaner()
