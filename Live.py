import CurrencyRouletteGame
import GuessGame
import MemoryGame
from Score import add_score


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."


def load_game():
    game = print_choose_text_and_get_chosen_number_with_range("Please choose a game to play:\n"
                                                              "1. Memory Game - a sequence of numbers will appear for 1"
                                                              " second and you have to guess it back\n"
                                                              "2. Guess Game - guess a number and see if you chose"
                                                              " like the computer\n"
                                                              "3. Currency Roulette - try and guess the value of"
                                                              " a random amount of USD in ILS\n", 1, 3)
    game_difficulty = print_choose_text_and_get_chosen_number_with_range("Please choose game difficulty from 1 to 5: ",
                                                                         1, 5)
    print(f"Chosen game: {game}, Difficulty: {game_difficulty}")
    if game == "1":
        is_user_won = MemoryGame.play(game_difficulty)
    if game == "2":
        is_user_won = GuessGame.play(game_difficulty)
    if game == "3":
        is_user_won = CurrencyRouletteGame.play(game_difficulty)

    if is_user_won:
        add_score(int(game_difficulty))
    return is_user_won


def print_choose_text_and_get_chosen_number_with_range(text, start_range, stop_range):
    options = list(map(str, range(start_range, stop_range + 1)))
    chosen_number = input(text)
    while chosen_number not in options:
        print("#### Wrong input ####")
        chosen_number = input(text)
    return chosen_number
