def prompt_guess() -> str:
    return input("Guess a letter: ").strip()

def print_status(state: dict) -> None:
    print("\nCurrent word:", ' '.join(state['display']))
    print(f"Wrong guesses: {state['wrong_guesses']}/{state['max_tries']}")
    print("Guessed letters:", ' '.join(sorted(state['guessed'])))

def print_result(state: dict) -> None:
    if '_' not in state['display']:
        print("\nYou won! The word was:", state['secret'])
    else:
        print("\nYou lost. The word was:", state['secret'])