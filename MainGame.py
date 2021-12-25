from Live import load_game, welcome

print(welcome("Guy"))
is_user_won = load_game()
if is_user_won:
    print("you won !")
else:
    print("you lost...")
