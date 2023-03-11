from random import randint


def header():
    """
    Gives a header with Current Mode and Rules for the player
    :return:
    """
    print("\t----- HANGMAN GAME ----- ")
    print("\t💩💩 Nutella mode 💩💩")

    print(""" 
          📃 RULES 📃
      ❕ You have 6 lifes
      ❕ Type "EXIT" to quit
    
    
    Choose a Word Theme:
        (A) Object
        (B) Body part
        (C) Food""")
    try:
        word_theme = input(" >> ").upper()
        validate_user_input(word_theme)
    except:
        print("Invalid value!")
    return word_theme


def validate_user_input(user_input):
    is_valid = True
    if user_input == " " or len(user_input) > 1 or len(user_input) < 1 or not user_input.isalpha():
        raise ValueError
        is_valid = False

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
    print("\t::LIFE::")
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
    print("""
============
|          §
|          §   
|
|
|""")
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


def win_game(place_letter):
    if "_" not in place_letter:
        end_game("\t\t🎉 YOU WON, CONGRATS! 🎉\n👿 But I really wish you had died.... 👿")


def end_game(msg):
    """
    Function to end the game in different cenarios
    :return:
    """
    print(msg)
    quit()
