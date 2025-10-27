from hangman.words import load_words, choose_secret_word
from hangman.game import (
    init_state, validate_guess, apply_guess,
    is_won, is_lost, render_display, render_summary
)
from hangman.io import prompt_guess, print_status, print_result
import os

def play(words_path: str, max_tries: int = 6) -> None:
    words = load_words(words_path)
    secret = choose_secret_word(words)
    state = init_state(secret, max_tries)
    print("Welcome to Hangman ")
    while True:
        print_status(state)
        guess = prompt_guess()
        valid, msg = validate_guess(guess, state['guessed'])
        if not valid:
            print(msg)
            continue
        apply_guess(state, guess)
        if is_won(state) or is_lost(state):
            print_status(state)
            print_result(state)
            break

if __name__ == "__main__":
    base_dir = os.path.join(os.path.dirname(__file__), 'data')
    words_file = os.path.join(base_dir, 'words.txt')
    play(words_file)