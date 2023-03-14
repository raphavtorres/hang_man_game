import functions as fc
import word_api
from collors import collors as col

level_choice = fc.header()
word_theme = ''
if level_choice != 'Root':
    word_theme = fc.get_theme(level_choice)


opt_add_rmv = None
if level_choice == 'Coffee with Milk':
    opt_add_rmv = fc.show_add_remove_opt()

if level_choice != 'Root':
    random_word, tip = fc.random_word(word_theme, opt_add_rmv, level_choice)
else:
    random_word, tip = word_api.get_api_random()
    # print(random_word)

# TIMER
if level_choice != 'Nutella':
    if level_choice == 'Coffee with Milk':
        fc.timer(30.0)
    else:
        fc.timer(20.0)

# Game time
game_time = fc.start_time_game()

# LIFE
hearts_list, life = fc.stars_life()

#  WRONG AND RIGHT LETTERS LISTS
wrong_letters = []
right_letters = []

placement_letters = fc.create_placement_letters(random_word)

while True:
    print("-" * 40)
    print(f"{col['blue']}CLUE: {tip}{col['clean']}")
    for heart in hearts_list:
        print(heart, end="")
    print(f" = {life}")

    print(f" {col['red-text']}||Wrong letters ❌: {wrong_letters}||{col['clean']}")

    fc.show_placement_letters(placement_letters)
    fc.win_game(placement_letters, game_time)

    try:
        user_input = input(">> ").lower()
        user_input = user_input.strip()

        if user_input == "exit":
            fc.end_game(f"{col['pink']}QUIT?? Too weak...{col['clean']}")

        is_valid = fc.validate_user_input(user_input)
        if is_valid:
            isCorrectLetter, life, wrong_letters = fc.letter_test(
                random_word, user_input, life, hearts_list, wrong_letters, right_letters)
            placement_letters = fc.change_placement_letters(random_word, isCorrectLetter,
                                                            placement_letters, user_input)

    except ValueError:
        print("Invalid input, dummy. Do it again! (Only ONE *letter*)")

    if life == 0:
        fc.loose_game(random_word)


# DESTACAR
# Mostrar temporizador para usuário

# biblioteca: inquirer
# Tentei : auto-py-to-exe; cxfreeze ((funcionou melhor)); pyinstaller
# NSIS --> tudo um arquivo só



    """
    api.dicionario.aberto.net ((pingo uma vez para palavra e outra para a dica (vem dentro de xml)))
    libs: requests
    """
