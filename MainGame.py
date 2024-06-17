from Live import welcome, load_game
import Score
import MainScores


print(welcome("Guy"))
load_game()
print("Your score is " + Score.read_score())
