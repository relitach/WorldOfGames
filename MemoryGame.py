import os
import random
import time
from Utils import screen_cleaner


def generate_sequence(difficulty):
    random_numbers = []
    for i in range(difficulty):
        random_numbers.append(random.randint(1, 100))
    print(random_numbers)
    return random_numbers


def get_list_from_user(difficulty):
    options = list(map(str, range(1, 101)))
    list_from_user = []
    for i in range(difficulty):
        number_to_list = input(f"Please enter number between 1 to 100 ({i + 1}/{difficulty}): ")
        while number_to_list not in options:
            print("#### Wrong input ####")
            number_to_list = input(f"Please enter numbers between 1 to 100: ")
        list_from_user.append(int(number_to_list))
    return list_from_user


def is_list_equal(random_numbers, list_from_user):
    print(f"Random numbers are: {random_numbers}")
    print(f"List from user are: {list_from_user}")
    random_numbers.sort()
    list_from_user.sort()
    if random_numbers == list_from_user:
        return True
    else:
        return False


def play(difficulty):
    print("#### Memory Game ####")
    random_numbers = generate_sequence(int(difficulty))
    time.sleep(0.7)
    screen_cleaner()
    list_from_user = get_list_from_user(int(difficulty))
    is_user_won = is_list_equal(random_numbers, list_from_user)
    return is_user_won


def clear_terminal():
    # os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    # because we run on Pycharm and not cmd ill do prints
    for i in range(20):
        print('\n')



