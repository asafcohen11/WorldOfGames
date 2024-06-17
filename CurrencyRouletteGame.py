import random, requests

def generate_random():
    return random.randint(1, 101)


def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url, verify=False)
    #print(f'response is {response}')
    rate = response.json()['rates']['ILS']
    #print (f'Rate is {rate}')
    return rate


def get_money_interval(num, usd_amount):
    #print(f'Ramdom number is {usd_amount}')
    rate = get_currency_rate()
    ils = rate * usd_amount
    offset = 5 - num
    #print(f"Offset {offset}" )
    return ils - offset, ils + offset


def get_guess_from_user(num):
    number = int(input(f"Who much are {num} USD in ILS? "))
    return number


def play(num):
    usd_amount = generate_random()
    min_interval, max_interval = get_money_interval(num, usd_amount)
    #print(f'min interval = {min_interval}, max interval = {max_interval}')
    num_from_user = get_guess_from_user(usd_amount)
    if min_interval <= num_from_user <= max_interval:
        return "You guessed right, you won the game"
    else:
        return "You guessed wrong, you lost the game"




#3play(2)
