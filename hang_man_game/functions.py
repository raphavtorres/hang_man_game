from random import randint
from collors import collors as col
import time
import inquirer
# libs to time
from threading import Timer
import os


def end_game(msg=f"\t{col['red-text']}💀 GAME OVER 💀{col['clean']}", secret_word=None):
    """
    Function to end the game in different scenarios
    :return:
    """
    if secret_word is not None:
        print(f"The secret word was: {secret_word}")

    print(msg)
    pid = os.getpid()
    os.kill(pid, -1)  # case problem change to 0


def timer(seconds_amount, secret_word):
    """
    Starts the timer
    :return:
    """
    timer_variable = Timer(seconds_amount, get_word(secret_word))
    timer_variable.start()


def start_time_game():
    game_time = time.time()
    return game_time


def loose_game(secret_word):
    end_game(secret_word)


# def time_end():
#     print(f"\t{col['red-text']}TIME'S UP ⏳{col['clean']}")
#     end_game()

def get_word(secret_word):
    def time_end():
        print(f"\t{col['red-text']}TIME'S UP ⏳{col['clean']}")
        end_game(secret_word=secret_word)
    return time_end


def input_style():
    """
    Controls input's bar style
    :return:
    """
    return f"{col['green-text']} >> {col['clean']}"


def game_level():
    """
    Choose game level (Nutella; Coffee with Milk; Root)
    :return:
    """
    questions = [
        inquirer.List('size',
                      message=f"{col['yellow']}CHOOSE YOUR LEVEL!{col['clean']}",
                      choices=['Nutella', 'Coffee with Milk', 'Root'],
                      ),
    ]

    level_choice = inquirer.prompt(questions)
    return level_choice['size']


def get_theme(level_choice):
    if level_choice != "Root":
        print(f"""
        {col['green-text']}
    Choose a Word Theme:
        (A) Object
        (B) Animal
        (C) Food{col['clean']}""")
        while True:
            try:
                word_theme = input(" >> ").upper()
                if word_theme == "EXIT":
                    end_game(f"{col['pink']}QUIT?? Too weak...{col['clean']}")
                is_valid = validate_user_input(word_theme)
                if is_valid and word_theme in "ABC":
                    return word_theme
                else:
                    raise ValueError
            except ValueError:
                print("Invalid value!")
                continue


def header():
    """
    Gives a header with Current Mode and Rules for the player
    :return:
    """
    level_choice = game_level()
    emoji = ''
    if level_choice == 'Nutella':
        emoji = '💩'
    elif level_choice == 'Coffee with Milk':
        emoji = '☕'
    elif level_choice == 'Root':
        emoji = '🌳'

    print(f"""
    {col['yellow-text']} ----- HANGMAN GAME ----- 
    {emoji}  {level_choice} mode {emoji} {col['clean']}""")

    print(f""" 
          📃 RULES 📃
      ❕ You have 6 lifes
      ❕ Type "EXIT" to quit
""")

    return level_choice


def validate_user_input(user_input):
    is_valid = True
    if user_input == " " or len(user_input) > 1 or len(user_input) < 1 or not user_input.isalpha():
        raise ValueError
    return is_valid


def show_add_remove_opt():
    questions = [
        inquirer.List('size',
                      message=f"{col['yellow']}CHOOSE AN OPTION: {col['clean']}",
                      choices=['Add Word', 'Remove Word', 'Continue'],
                      ),
    ]

    choice = inquirer.prompt(questions)
    return choice['size']


def validate_add_remove(user_input):
    is_valid_input = True
    if len(user_input) < 1 or not user_input.isalpha():
        raise ValueError
    else:
        return is_valid_input


def add_remove_word(opt_add_rmv, words, word_tip):
    for i in range(2):
        # print(f"Words: {words}")
        # print(f"Words tips: {word_tip}")
        if opt_add_rmv == "Add Word":
            while True:
                try:
                    new_word = input("New Word >> ").lower().strip()
                    valid_new_word = validate_add_remove(new_word)

                    new_word_tip = input("New word's tip >> ").lower().strip()
                    valid_tip = validate_add_remove(new_word_tip)

                    if valid_new_word and valid_tip and new_word not in words:
                        words.append(new_word)
                        word_tip.append(new_word_tip)
                        break
                    else:
                        print("WORD ALREADY IN LIST OF WORDS")
                        raise ValueError
                except ValueError:
                    print("Invalid value!")
                    continue
        elif opt_add_rmv == "Remove Word":
            while True:
                try:
                    word_remove_index = input("Position of word to remove >> ").strip()
                    if len(word_remove_index) == 1 or not word_remove_index.isdecimal():
                        int_word_remove_index = int(word_remove_index) - 1
                        if int_word_remove_index < len(words):
                            words.pop(int_word_remove_index)
                            word_tip.pop(int_word_remove_index)
                            break
                        else:
                            print("WORD NOT IN LIST OF WORDS")
                            raise ValueError
                except ValueError:
                    print("Invalid value!")
                    continue
        if i == 1:
            break

        another = ''
        if opt_add_rmv == "Add Word":
            another = input("1/2 words taken. Want's to remove one more? [Y/N]: ").lower()
        elif opt_add_rmv == "Remove Word":
            another = input("1/2 new words. Want's to put one more? [Y/N]: ").lower()
        if another != "y":
            break


def random_word(word_theme, opt_add_rmv, level_choice):
    """
    Returns a random word | Has a database of words and hints
    :return:
    """

    # Themes: Object, Body part, Food
    object_words = ['pencil', 'pillow', 'blanket', 'whiteboard', 'toothbrush']
    animal_words = ['donkey', 'cheetah', 'squirrel', 'elephant', 'salamander']
    food_words = ['spaghetti', 'yoghurt', 'biryani', 'pineapple', 'gingerbread']

    # Themes Tips:
    object_word_tip = ['used in writing', 'for your head', 'to cover', 'you write on it', 'used in personal cleaning']
    animal_word_tip = ['looks like a horse', 'looks like a cat', 'looks like a mouse', 'is big', 'looks like a lizard']
    food_word_tip = [
        'a type of pasta',
        'a semi-solid food item made from fermented milk',
        'a food item made with seasoned rice, vegetables and sometimes meat',
        'a fruit surrounded by tough segmented skin',
        'cake made with molasses (molasses is thick, dark brown syrup)'
    ]
    words = [" "]
    word_tip = [" "]

    if word_theme == "A":
        words = object_words.copy()
        word_tip = object_word_tip.copy()
    elif word_theme == "B":
        words = animal_words.copy()
        word_tip = animal_word_tip.copy()
    elif word_theme == "C":
        words = food_words.copy()
        word_tip = food_word_tip.copy()

    if level_choice == "Coffee with Milk":
        add_remove_word(opt_add_rmv, words, word_tip)

    rand_index = randint(0, len(words) - 1)
    random_word_var = words[rand_index]
    tip = word_tip[rand_index]

    return random_word_var, tip


def loose_life(life, hearts_list):
    """
    Function used to reduce amount of life
    :param life: Amount of life
    :param hearts_list: Visual of life amount
    :return:
    """
    life -= 1
    hearts_list.remove(" ❤ ")
    return life


def stars_life():
    """
    Starts amount of life and creates visual "life" element
    :return:
    """
    life = 6
    hearts_list = [" ❤ "] * life

    return hearts_list, life


def create_placement_letters(rand_word):
    place_letters = ["_"] * len(rand_word)
    return place_letters


def change_placement_letters(random_word_var, is_correct_letter, place_letters, user_input):
    """
    Creates a visual control of the game to the player | Changes the placement letters
    :param:
    :return:
    """
    if is_correct_letter:
        for i, place in enumerate(place_letters):
            if random_word_var[i] == user_input:
                place_letters[i] = user_input
    return place_letters


def show_placement_letters(place_letters):
    print(f"""{col['yellow-text']}
============
|          §
|          §   
|
|
|{col['clean']}""")
    print("| ", end="")
    for place in place_letters:
        print(place, end=" ")
    print("")


def letter_test(random_word_var, user_input, life, hearts_list, wrong_letters, right_letters):
    """
    Tests if the letter is in "game word" or not
    :return: isCorrectLetter | bool
    """
    is_correct_letter = False
    msg_used_letter = f"You already tried the letter {user_input.upper()}..."
    if user_input not in random_word_var:
        if user_input in wrong_letters:
            print(msg_used_letter)
        else:
            life = loose_life(life, hearts_list)
            wrong_letters.append(user_input)
    else:
        if user_input in right_letters:
            print(msg_used_letter)
        else:
            is_correct_letter = True
            right_letters.append(user_input)
    return is_correct_letter, life, wrong_letters


def win_game(place_letter, game_time, secret_word):
    if "_" not in place_letter:
        print(f"\n{col['green-text']}You took {int(time.time() - game_time)} seconds to finish!{col['clean']}")
        end_game(f"\t{col['green']}🎉 YOU WON, CONGRATS! 🎉{col['clean']}", secret_word=secret_word)
