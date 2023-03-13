import requests


def get_api_random():
    while True:
        word_url = "https://random-word-api.herokuapp.com/word?number=1"
        word_response = requests.get(word_url)
        word = word_response.json()[0]

        definition_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        definition_response = requests.get(definition_url)

        try:
            definition = definition_response.json()[0]['meanings'][0]['definitions'][0]['definition']
        except KeyError:
            continue
        break

    return word, definition

# 'title': 'No Definitions Found'

# if 'No Definitions Found' not in definition_response.json():
# print(word)
# print(definition_response.json())
