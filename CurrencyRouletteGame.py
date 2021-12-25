import random

from currency_converter import CurrencyConverter


def get_money_interval(difficulty, total_value):
    money_interval = (total_value - (5 - difficulty), total_value + (5 - difficulty))
    return money_interval


def get_guess_from_user(usd_amount_random_number):
    number_to_list = input(f"Guess the value of {usd_amount_random_number} USD in ILS: ")
    while is_user_input_is_number(number_to_list) == False:
        print("#### Wrong input ####")
        number_to_list = input(f"Guess the value of {usd_amount_random_number} USD in ILS: ")
    return number_to_list


def is_user_input_is_number(input_str):
    try:
        # Convert it into integer
        val = int(input_str)
        # print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input_str)
            # print("Input is a float  number. Number = ", val)
            return True
        except ValueError:
            print("No.. input is not a number. It's a string")
            return False


def play(difficulty):
    print("#### Currency Roulette Game ####")
    c = CurrencyConverter()
    usd_amount_random_number = random.randint(1, 100)
    total_value = c.convert(usd_amount_random_number, 'USD', 'ILS')
    money_interval = get_money_interval(int(difficulty), total_value)
    guess_number= get_guess_from_user(usd_amount_random_number)
    print(f"random_number: {usd_amount_random_number}")
    print(f"total: {total_value}")
    print(f"money_interval: {money_interval}")
    if money_interval[0] <= float(guess_number) <= money_interval[1]:
        return True
    else:
        return False
