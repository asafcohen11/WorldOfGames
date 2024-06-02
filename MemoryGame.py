import random, time
"""
generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be difficulty.
2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of difficulty.
3. is_list_equal - A function to compare two lists if they are equal. The function will return
True / False.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won
"""

def generate_sequence(num):
    return [random.randint(1, 101) for _ in range(num)]


def get_list_from_user(num):
    user_list = []
    while len(user_list) < num:
        try:
            number = int(input(f"Enter number {len(user_list) + 1}: "))
            user_list.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return user_list


def s_list_equal(list1, list2):
    return list1 == list2


def play(num):
    generated_list = generate_sequence(num)
    print(generated_list, end='', flush=True)
    time.sleep(0.7)
    print("\r", end='', flush=True)  # This clears the printed text after the duration
    user_list = get_list_from_user(num)
    return s_list_equal(generated_list, user_list)

#print(play(3))
