from random import randint
import functions as fc
from collors import collors as col

word_theme = fc.header()

random_word, tip = fc.random_word(word_theme)

# print(random_word)
# print(word_theme)

print(f"{col['blue']}CLUE: {tip}{col['clean']}")

# LIFE
hearts_list, life = fc.stars_life()

# TIMER
fc.timer(3.0)  # 20 pro hard

# Game time
game_time = fc.startTimeGame()

#  WRONG AND RIGHT LETTERS LISTS
wrong_letters = []
right_letters = []

placement_letters = fc.create_placement_letters(random_word)

while True:
    print("-" * 40)
    for heart in hearts_list:
        print(heart, end="")
    print("")

    print(f" {col['red']}||Wrong letters ❌: {wrong_letters}||{col['clean']}")

    fc.show_placement_letters(placement_letters)
    fc.win_game(placement_letters, game_time)

    try:
        user_input = input(">> ").lower()
        user_input = user_input.strip()

        if user_input == "exit":
            fc.end_game(f"{col['pink']}QUIT?? Too weak...{col['clean']}")

        is_valid = fc.validate_user_input(user_input)
        if is_valid:
            isCorrectLetter, life, wrong_letters = fc.letter_test(random_word, user_input, life, hearts_list,
                                                                         wrong_letters, right_letters)
            placement_letters = fc.change_placement_letters(random_word, isCorrectLetter, placement_letters,
                                                                   user_input)
    except ValueError:
        print("Invalid input dummy. Do it again! (Only ONE *letter*)")

    if life == 0:
        fc.loose_game()


# DESTACAR
# Caso a pessoa erre, falar qual era a palavra
# Separar níveis
# Colocar o tempo que a pessoa demorou para terminar
# Mostrar temporizador para usuário
# Opção de colocar e remover palavras

# biblioteca inquirer (só funciona para exe)
    # Tentei : auto-py-to-exe; cxfreeze ((funcionou melhor)); pyinstaller
    # NSIS --> tudo um arquivo só

#  ===========
#  3 modos de jogo - Nutela / Café com leite / Raiz

# Café com leite
# Opção de adcionar ou remover palavras / dicas
# Tempo de jogo ==> 30 seg

# Raiz
# Palavras trazidas de uma API
# tempo de jogo == 20 seg (opcional - Thread)
#  Como trabalhar com API:

    """
    api.dicionario.aberto.net ((pingo uma vez para palavra e outra para a dica (vem dentro de xml)))
    libs: requests
    """

