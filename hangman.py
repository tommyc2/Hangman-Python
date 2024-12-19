# ================================
# Tommy Condon
# Hangman Python Assignment
# 20101841
# ================================

# Note: For this assignment, both a console app and GUI were created. The app is controlled via the terminal but the user switch between windows to see the changes made to the GUI (e.g. Hangman setup)

import random
import sys
import threading
import tkinter
import os

easy_words_list = []
normal_words_list = []
difficult_words_list = []
words_file = "english-nouns.txt"
window = None
image_label = None

# ================
# Main function
# ================
# -> Executes the starting program

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
    print("1. Easy\n2. Normal\n3. Difficult\n\n")

    difficulty = validate_input()

    if difficulty == 1:
        print("\nYou chose the Easy difficulty.")
        play_game(easy_words_list)
    elif difficulty == 2:
        print("\nYou chose the Normal difficulty.")
        play_game(normal_words_list)
    elif difficulty == 3:
        print("\nYou chose the Difficult difficulty.")
        play_game(difficult_words_list)

# Reads words from the passed in file
# Returns list with every word from file
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

# Initiates the game (GUI + console app)
def play_game(words):
    print("Picking a word.....please wait a moment")
    
    chosen_word = random.sample(words, 1)
    chosen_word = chosen_word[0]
    num_of_guesses_left = 6
    progress = [] # this is compared with the size of the correct word to check if the user has guessed all the words

    print(f"\n{chosen_word}\n") # testing purposes

    print(f"> Guess the letters in this {len(chosen_word)} letter word. Please enter 1 letter at a time.")
    
    while (num_of_guesses_left > 0):

        guess = str(input(">    ")).lower()
    
        if len(guess) == 1:
            if guess in chosen_word:
                print(f"'{guess.upper()}' is in the word!")
                print(f"This letter occurs {get_letter_occurences(guess,chosen_word)} time(s).")
                progress.append(get_letter_occurences(guess,chosen_word))

                if len(progress) == len(chosen_word):
                    print(f"\nYou've guessed all the letters!!\n The word was {str(chosen_word).upper()}")
                    window.destroy()

                num_of_guesses_left -= 1
                update_image(num_of_guesses_left)
                print(f"Remaining Guesses: {num_of_guesses_left}")
            else:
                num_of_guesses_left -= 1
                update_image(num_of_guesses_left)
                print(f"Guess is wrong. You have {num_of_guesses_left} remaining")
        else:
            print("You can only enter 1 letter at a time. Please try again")

    print("You have run of out of guesses. You now have UNLIMITED attempts at guessing the word!")

    word_guessed_is_right = False

    while (word_guessed_is_right == False):
        guessed_word = str(input(">   ")).lower()
        if(guessed_word == chosen_word):
            print("Hurray! You've guessed the word right!")
            print(f"The word was in fact '{guessed_word}'")
            word_guessed_is_right = True
            window.destroy()
        else:
            print("Wrong! Please try again!")

# Update the image in the image label for tkinter
# The image will be updated to the appropriate image required
def update_image(lives_left):
    global window
    global image_label
    
    if (lives_left == 1) or (lives_left == 2) or (lives_left == 0):
        image_path = f"images/{lives_left}.png"
        new_image = tkinter.PhotoImage(file=image_path)
        image_label.config(image=new_image)
        image_label.image = new_image
    else:
        image_path = f"images/{lives_left}.png"
        new_image = tkinter.PhotoImage(file=image_path).zoom(2,2)
        image_label.config(image=new_image)
        image_label.image = new_image

def get_letter_occurences(letter, right_word):
    counter = 0
    for i in range(len(right_word)):
        if right_word[i] == letter:
            counter += 1
    return counter
        
# Creates 3 separate lists for the game: easy, normal & difficult lists.
# Returns the 3 lists
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

# Validates the user input.
# If the user types in a number other than 1,2 or 3, the app will keep telling the user that they must enter a number between 1-3
def validate_input():
    while True:
        user_choice = int(input("> Enter an option above (1-3):    "))

        if (user_choice >= 1) and (user_choice <= 3):
            return int(user_choice) # e.g the number
        else:
            print("The number must be between 1-3. Please try again.")

# Sets up the tkinter GUI window in a separate space. The app is controlled via the terminal and the images are displayed via the GUI for the user to see
def setup_tkinter():
    global window
    global image_label

    window = tkinter.Tk()
    window.title("Tommy's Hangman Game")
    window.geometry("500x500")
    starter_image = tkinter.PhotoImage(file=f"images/{6}.png").zoom(2,2)
    image_label = tkinter.Label(window, image=starter_image)
    image_label.image = starter_image
    image_label.pack()
    window.mainloop()

# If the script is directly executes manually, execute this piece of code:
if __name__ == "__main__":
    main_thread = threading.Thread(target=main, daemon=True) # terminal based thread set up.
    main_thread.start()

    setup_tkinter()