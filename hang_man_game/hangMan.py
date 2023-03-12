from random import randint
import functions

word_theme = functions.header()

random_word, tip = functions.random_word(word_theme)
print(random_word)
print(word_theme)

print(f"CLUE: {tip}")

#  LIFE
hearts_list, life = functions.stars_life()

#  WRONG AND RIGHT LETTERS LISTS
wrong_letters = []
right_letters = []

placement_letters = functions.create_placement_letters(random_word)

while True:
    print("-" * 40)
    for heart in hearts_list:
        print(heart, end="")
    print("")

    print(f" ||Wrong letters ❌: {wrong_letters}||")

    functions.show_placement_letters(placement_letters)
    functions.win_game(placement_letters)

    try:
        user_input = input(">> ").lower()
        user_input = user_input.strip()

        if user_input == "exit":
            functions.end_game("QUIT?? Too weak...")

        is_valid = functions.validate_user_input(user_input)
        if is_valid:
            isCorrectLetter, life, wrong_letters = functions.letter_test(random_word, user_input, life, hearts_list,
                                                                         wrong_letters, right_letters)
            placement_letters = functions.change_placement_letters(random_word, isCorrectLetter, placement_letters,
                                                                   user_input)
    except ValueError:
        print("Invalid input dummy. Do it again! (Only ONE *letter*)")

    if life == 0:
        functions.end_game("\t\t💀 GAME OVER 💀\n🔥 You've died, see you in HELL! 🔥")



# DESTACAR
# Colocar cor no código
# Colocar temporizador no código

#  biblioteca inquirer (só funciona para exe)
    # Tentei : auto-py-to-exe; cxfreeze ((funcionou melhor)); pyinstaller
    # NSIS --> tudo um arquivo só

#  ===========
#  3 modos de jogo - Nutela / Café com leite / Raiz

#  Café com leite
#  opção de adcionar ou remover palavras / dicas
#  tempo de jogo ==> 30 seg

# Raiz
# Palavras trazidas de uma API
# tempo de jogo == 20 seg (opcional - Thread)
#  Como trabalhar com API:

    """
    api.dicionario.aberto.net ((pingo uma vez para palavra e outra para a dica (vem dentro de xml)))
    libs: requests
    
    """

