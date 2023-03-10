from random import randint
import funcoes

#  Jogo da forca
print("\t----- HANGMAN GAME ----- ")
print("\t💩💩 Nutella mode 💩💩")

print(""" 
📃 RULES 📃
    * 
    * Click "@" to quit
""")

#  LIFE == 6
life = ["🧡", "🧡", "🧡", "🧡", "🧡", "🧡"]
print("\t::LIFE::")
for heart in life:
    print(heart, end="")
print("")

#  DICAS DE PALAVRAS E PALAVRAS
words = ['pencil', 'telegraph', 'elbow']
word_tip = ['used in writing', 'ancient method for communication', 'body part']


random_word = words[randint(0, len(words) - 1)]
print(random_word)
#  Lista de letras erradas
wrong_letters = []

#  Lista de letras corretas
right_letters = []

placement_letters = []
for letter in random_word:
    placement_letters.append("_")

for place in placement_letters:
    print(place, end="")
print("")

while True:
    try:
        user_input = input(">> ")
    except ValueError:
        print("Invalid input dummy. Do it again!")

    # if user_input in placement_letters:
    #     placement_letters[]
    if user_input == "@":
        quit()


#  * Palavras e Dicas - Lista
#  Letra que já foi, não é mais aceita (não perde mais vida)
    #  Mesma coisa com letras certas
#  Letras maiusculas e minusculas



#  DESTACAR
#  Utilizar o máximo de funções e sempre comentá-las
#  Fazer em ing
#  Mostrar letras já utilizadas
#  Colocar tema de palavras

#  biblioteca inquirer (só funciona para exe)
#  auto-py-to-exe 2.32.0

#  ===========
#  3 modos de jogo - Nutela / Café com leite / Raiz
#  Nutela


#  Café com leite
#  opção de adcionar ou remover palavras / dicas
#  tempo de jogo ==> 30 seg

# Raiz
# Palavras trazidas de uma API
# tempo de jogo == 20 seg (opcional - Thread)
#  Como trabalhar com API:
    '''
    api.dicionario.aberto.net ((pingo uma vez para palavra e outra para a dica (vem dentro de xml)))
    libs: requests
    
    '''

