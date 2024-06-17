import random


# - Will generate number between 1 to difficulty and save it to secret_number.
def generate_number(upper_limit):
    x = random.randint(1, upper_limit)
    #print(x)
    return x


# - Will prompt the user for a number between 1 to difficulty and return the number.
def get_guess_from_user(upper_limit):
    return int(input(f"Enter a number between 1 and {upper_limit}: "))


# - Will compare the secret generated number to the one prompted by the get_guess_from_user.
def compare_results(user_number, random_number):
    return user_number == random_number


# - Will call the functions above and play the game. Will return True / False if the user lost or won.
def play(difficulty):
    random_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    return compare_results(user_number, random_number)


#print(play(3))
