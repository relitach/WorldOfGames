import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty)+1)
    return secret_number


def get_guess_from_user(difficulty):
    options = list(map(str, range(1, int(difficulty) + 1 + 1)))
    guess_number = input(f"Please enter your guess between 1 to {int(difficulty)+1}: ")
    while guess_number not in options:
        print("#### Wrong input ####")
        guess_number = input(f"Please enter your guess between 1 to {int(difficulty)+1}: ")
    return guess_number


def compare_results(secret_number, guess_number):
    print(f"Secret number is: {secret_number}")
    print(f"Guess number is: {guess_number}")
    if secret_number == int(guess_number):
        return True
    else:
        return False


def play(difficulty):
    print("#### Guess Game ####")
    secret_number = generate_number(difficulty)
    guess_number = get_guess_from_user(difficulty)
    is_user_won = compare_results(secret_number, guess_number)
    return is_user_won
