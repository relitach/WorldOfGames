from Utils import SCORES_FILE_NAME
import os


def add_score(difficulty):
    current_score = "0"
    point_of_score = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, "r") as file:
            current_score = file.read()
        scores_file = open(SCORES_FILE_NAME, "w")
    else:
        print(f"File {SCORES_FILE_NAME} not exist. creating new one")
        scores_file = open(SCORES_FILE_NAME, "w")

    print(f"Current score in file is: {current_score}")
    new_score = int(current_score) + point_of_score
    print(f"Writing new score: {new_score} to {SCORES_FILE_NAME}")
    scores_file.write(f"{new_score}")
    scores_file.close()