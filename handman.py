import random
import os
from re import L

def read_data():
    try:
        words = []
        with open('./archivos/data.txt','r',encoding='utf-8') as f:
            for word in f:
                words.append(word.strip().upper())
        return words 
    except FileNotFoundError:
        print ('The file doesnt exist, please check the path')

def chosen_word(word):
    random_word = random.choice(word)
    print(random_word)
    return random_word


def normalize(word): # Change the accent for vowels
    word1 = word.maketrans('ÁÉÍÓÚÑ','AEIOUN')
    word = word.translate(word1)
    return word

def hide_word(word):
    letter_index_dict= {}
    num_let = [letter for letter in word]
    underscores = ['_'] * len(num_let)

    for idx, letter in enumerate(word):
        # print(f'{idx} --- {letter}')
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = [] #A space within dict is created to store the new letter
            print(letter_index_dict)
        letter_index_dict[letter].append(idx) # Created space is assigned the index
        # print(letter_index_dict[letter])

    print(letter_index_dict)

    input_msg = """
  _   _                                                                      _ 
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __     __ _  __ _ _ __ ___   ___| |
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   / _` |/ _` | '_ ` _ \ / _ \ |
 |  _  | (_| | | | | (_| | | | | | | (_| | | | | | (_| | (_| | | | | | |  __/_|
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \__, |\__,_|_| |_| |_|\___(_)
                    |___/                         |___/                        
    """


    while True:
        os.system('cls')
        print(input_msg)
        print(f'Guess the word with {len(word)} letters!')
        for element in underscores:
            print(element + ' ', end='')
        print('\n')

        letter_input = input('Type a letter here: ').strip().upper()
        assert letter_input.isalpha(), 'Only letters are allowed' 

        if letter_input in num_let: # Validate if the input letter is in the word
            for idx in letter_index_dict[letter_input]:
                underscores[idx] = letter_input

        if '_' not in underscores:
            os.system('cls')
            print(f"You got it! Congrats :D\n The guess word was {word}")
            break


def run():
    guess_word = chosen_word(read_data())
    guess_word_norm = normalize(guess_word)
    hide_word(guess_word_norm)


if __name__ == '__main__':
    run()