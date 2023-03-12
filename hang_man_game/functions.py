from random import randint
from collors import collors as col
import time

# libs to time
from threading import Timer
import os


def end_game(msg=f"\t\t{col['red']}💀 GAME OVER 💀{col['clean']}\n🔥 {col['red-text']}You've died, see you in HELL! {col['clean']}🔥"):
    """
    Function to end the game in different scenarios
    :return:
    """
    print(msg)
    pid = os.getpid()
    os.kill(pid, 0)
    # exit()


def timer(seconds_amount):
    """
    Starts the timer
    :return:
    """
    timer = Timer(seconds_amount, time_end)
    timer.start()


def startTimeGame():
    game_time = time.time()
    return game_time


def loose_game():
    end_game()


def time_end():
    print(f"\t\t{col['red-text']}TIME'S UP ⏳{col['clean']}")
    end_game()


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
    print(f"""{col['yellow']}CHOOSE YOUR LEVEL!
    (A) Nutella 💩
    (B) Coffee with Milk ☕
    (C) Root 🌳
{col['clean']}""")
    try:
        level_choice = input(input_style()).upper()

        validate_user_input(level_choice)
        is_valid = validate_user_input(level_choice)
        if is_valid and level_choice in "ABC":
            if level_choice == "A":
                return 'Nutella', '💩'
            elif level_choice == "B":
                return 'Coffee with Milk', '☕'
            elif level_choice == "C":
                return 'Root', '🌳'
        else:
            raise ValueError
    except ValueError:
        print("Invalid value!")


def header():
    """
    Gives a header with Current Mode and Rules for the player
    :return:
    """
    level_choice, emoji = game_level()
    print(f"""
    {col['yellow-text']} ----- HANGMAN GAME ----- 
     {emoji} {level_choice} mode {emoji} {col['clean']}""")

    print(f""" 
          📃 RULES 📃
      ❕ You have 6 lifes
      ❕ Type "EXIT" to quit
    
    {col['green-text']}
    Choose a Word Theme:
        (A) Object
        (B) Body part
        (C) Food{col['clean']}""")
    while True:
        try:
            word_theme = input(" >> ").upper()
            if word_theme == "EXIT":
                end_game(f"{col['pink']}QUIT?? Too weak...{col['clean']}")

            validate_user_input(word_theme)
            is_valid = validate_user_input(word_theme)
            if is_valid and word_theme in "ABC":
                return word_theme
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid value!")
            continue


def validate_user_input(user_input):
    is_valid = True
    if user_input == " " or len(user_input) > 1 or len(user_input) < 1 or not user_input.isalpha():
        is_valid = False
        raise ValueError

    return is_valid


def random_word(word_theme):
    """
    Returns a random word | Has a database of words and hints
    :return:
    """

    # Themes: Object, Body part, Food
    object_words = ['pencil', 'telegraph', 'elbow']
    animal_words = ['animal']
    food_words = ['food']

    # Themes Tips:
    object_word_tip = ['used in writing', 'ancient method for communication', 'body part']
    animal_word_tip = ['animal']
    food_word_tip = ['food']
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

    rand_index = randint(0, len(words) - 1)
    random_word = words[rand_index]
    tip = word_tip[rand_index]

    return random_word, tip


def loose_life(life, hearts_list):
    """
    Function used to reduce amount of life
    :param life: Amount of life
    :param hearts_list: Visual of life amount
    :return:
    """
    life -= 1
    hearts_list.insert(1, "🖤")
    hearts_list.remove("🧡")
    hearts_list.sort(reverse=True)
    return life


def stars_life():
    """
    Starts amount of life and creates visual "life" element
    :return:
    """
    life = 6
    hearts_list = ["🧡"] * life

    return hearts_list, life


def create_placement_letters(rand_word):
    place_letters = ["_"] * len(rand_word)
    return place_letters


def change_placement_letters(random_word, isCorrectLetter, place_letters, user_input):
    """
    Creates a visual control of the game to the player | Changes the placement letters
    :param rand_word:
    :return:
    """
    if isCorrectLetter:
        for i, place in enumerate(place_letters):
            if random_word[i] == user_input:
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


def letter_test(random_word, user_input, life, hearts_list, wrong_letters, right_letters):
    """
    Tests if the letter is in "game word" or not
    :return: isCorrectLetter | bool
    """
    isCorrectLetter = False
    msg_used_letter = f"You already tried the letter {user_input.upper()}..."
    if user_input not in random_word:
        if user_input in wrong_letters:
            print(msg_used_letter)
        else:
            life = loose_life(life, hearts_list)
            wrong_letters.append(user_input)
    else:
        if user_input in right_letters:
            print(msg_used_letter)
        else:
            isCorrectLetter = True
            right_letters.append(user_input)
    return isCorrectLetter, life, wrong_letters


def win_game(place_letter, game_time):
    if "_" not in place_letter:
        print(f"\n{col['green-text']}You took {int(time.time() - game_time)} seconds to finish!{col['clean']}")
        end_game(f"\t\t🎉{col['green']} YOU WON, CONGRATS! {col['clean']}🎉\n👿 {col['red-text']}"
                 f"But I really wish you had died... 👿{col['clean']}")
