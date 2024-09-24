########################################
# Name: Myles Crandall
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 0.75
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    current_row = 0
    N_ROWS = 6

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        # Get the current guess from the current row
        guess = word_from_row(current_row).upper()

        if len(guess) == N_COLS and is_english_word(guess.lower()):
            gw.show_message("That's a 5 letter English word")  # Show message for correct guess
        else:
            gw.show_message("Not in word list")  # Show message for invalid words


    def word_from_row(row):
        # Get the word from a specific row
        word = ""
        for col in range(N_COLS):
            letter = gw.get_square_letter(row, col)
            word += letter
        return word


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
