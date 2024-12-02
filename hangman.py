# ================================
# Tommy Condon
# Hangman Python Assignment
# 20101841
# ================================

import random

easy_words_list = []
normal_words_list = []
difficult_words_list = []

words_file = "english-nouns.txt"

def main():
    global easy_words_list
    global difficult_words_list
    global normal_words_list

    words_list = read_words_from_file(words_file)

    if len(words_list) == 0:
        return

    easy_words_list, normal_words_list, difficult_words_list = create_lists(words_list)

    #print("Easy List", easy_words_list)
    #print("Normal: ", normal_words_list)
    #print("Difficult: ", difficult_words_list)

    print("-------------------")
    print("---- Main Menu ----")
    print("-------------------")

    print("\nChoose your difficulty level:\n")

    difficulty = int(input("1. Easy\n2. Normal\n3. Difficult\n\nEnter your choice -->     "))

    if difficulty == 1:
        print("\nYou chose the Easy difficulty.")
        play_game(easy_words_list)
    elif difficulty == 2:
        print("\nYou chose the Normal difficulty.")
        play_game(normal_words_list)
    elif difficulty == 3:
        print("\nYou chose the Difficult difficulty.")
        play_game(difficult_words_list)

def read_words_from_file(file_name):
    list_of_words_to_return = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                word = line.strip()
                if word:
                    list_of_words_to_return.append(word)
        return list_of_words_to_return # returning list of found words in file
    except Exception as e:
        print("Error:", e)

def play_game(words):
    print(words)

def create_lists(words_list):
    a = []
    b = []
    c = []

    for word in words_list:
        if len(word) >= 2 and len(word) <= 5:
            a.append(word)
        elif len(word) >= 6 and len(word) <= 8:
            b.append(word)
        elif len(word) > 8:
            c.append(word)

    a = list(set(a))
    b = list(set(b))
    c = list(set(c))

    a = random.sample(a, min(len(a), 20)) # I did this to make sure that if there wasn't 20 words in a particular list, it would take the lowest value instead
    b = random.sample(b, min(len(b), 20))
    c = random.sample(c, min(len(c), 20))

    return a, b, c

    
def validate_input():
    pass

main()