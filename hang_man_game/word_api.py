import requests

# PROXIES = {
#     ...
# }


def get_api_random():
    while True:
        word_url = "http://random-word-api.herokuapp.com/word?number=1"
        word_response = requests.get(word_url) #, proxies=PROXIES)
        word = word_response.json()[0]

        definition_url = f"http://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        definition_response = requests.get(definition_url) #, proxies=PROXIES)

        try:
            definition = definition_response.json()[0]['meanings'][0]['definitions'][0]['definition']
        except KeyError:
            continue
        break

    return word, definition
