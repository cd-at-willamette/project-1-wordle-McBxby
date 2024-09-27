########################################
# Name: Myles Crandall
# Collaborators (if any): 
# GenAI Transcript (if any): Got help from ChatGPT for the color_row function specifically remaining letters equal to the target word
# Estimated time spent (hr): 6.0
# Description of any added extensions: I asked ChatGPT to help me with adding "Welcome to Myles's Worlde!" at the top of the game.
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        current_row = gw.get_current_row() # Get the current row
        guess = word_from_row(current_row).upper() # Get the current guess from the current row
        if len(guess) == N_COLS and is_english_word(guess.upper()): # Check if the guess is a valid 5-letter English word
            color_row(current_row, guess) # Color the row based on the guess
            gw.show_message("That's a 5 letter English word") # Show message for correct guess
            if guess == secret_word: # If the guess is the target word
                gw.show_message("Congratulations! You've won!") # Show message for winning
                gw.set_current_row(N_ROWS) # Set the current row to the last row
            elif gw.get_current_row() == N_ROWS - 1: # If the current row is the last row
                gw.show_message(f"Game over. The word was {secret_word}") # Show message for losing
                gw.set_current_row(N_ROWS) # Set the current row to the last row
            else: # If the guess is not the target word
                gw.set_current_row(current_row + 1) # Set the current row
        else: # If the guess is not valid
            gw.show_message("Not in word list") # Show message for invalid words

    def word_from_row(row): # Get the word from a specific row
        word = "" # Initialize the word
        for col in range(N_COLS): # Iterate through each column in the row
            letter = gw.get_square_letter(row, col) # Get the letter at the current row and column
            word += letter # Add the letter to the word
        return word # Return the word
    
    def color_row(row, guess): # Color the row based on the guess
        remaining_letters = list(secret_word) # Initialize the remaining letters
        for col in range(N_COLS): # Iterate through each column in the row
            letter = guess[col] # Get the letter at the current column
            if letter == secret_word[col]: # If the letter is in the correct position
                gw.set_square_color(row, col, CORRECT_COLOR) # Set the color of the square to CORRECT_COLOR
                gw.set_key_color(letter, CORRECT_COLOR) # Set the color of the key to CORRECT_COLOR
                remaining_letters[col] = None # Remove the letter from the remaining letters
    
        for col in range(N_COLS): # Iterate through each column in the row
            letter = guess[col] # Get the letter at the current column
            if gw.get_square_color(row, col) != CORRECT_COLOR: # If the letter is not in the correct position
                if letter in remaining_letters: # If the letter is in the target word
                    gw.set_square_color(row, col, PRESENT_COLOR) # Set the color of the square to PRESENT_COLOR
                    if gw.get_key_color(letter) != CORRECT_COLOR: # If the key is not CORRECT_COLOR
                        gw.set_key_color(letter, PRESENT_COLOR) # Set the color of the key to PRESENT_COLOR
                    remaining_letters[remaining_letters.index(letter)] = None # Remove the letter from the remaining letters
                else: # If the letter is not in the target word
                    gw.set_square_color(row, col, MISSING_COLOR) # Set the color of the square to MISSING_COLOR
                    if gw.get_key_color(letter) == UNKNOWN_COLOR: # If the key is UNKNOWN_COLOR
                        gw.set_key_color(letter, MISSING_COLOR) # Set the color of the key to MISSING_COLOR
 
    def five_letter_word(): # Get a random 5-letter word from the English word list
        random.shuffle(ENGLISH_WORDS) # Shuffle the English word list
        for word in ENGLISH_WORDS: # Iterate through each word in the English word list
            if len(word) == 5 and not word.endswith('s'): # If the word is 5 letters long and does not end with 's' (to avoid plurals) 
                return word.upper() # Return the word

    secret_word = five_letter_word() # Get a random 5-letter word from the English word list and convert it to uppercase
    print(secret_word) # Print the secret word

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup boilerplate
if __name__ == "__main__":
    wordle()
