from typing import Dict, Set, Tuple

def init_state(secret: str, max_tries: int) -> Dict:
    display = ['_' for _ in secret]
    return {
        "secret": secret,
        "display": display,
        "guessed": set(),
        "wrong_guesses": 0,
        "max_tries": max_tries
    }

def validate_guess(ch: str, guessed: Set[str]) -> Tuple[bool, str]:
    if not ch or len(ch) != 1:
        return False, "Please enter one letter only."
    if ch in guessed:
        return False, "You already guessed that letter."
    return True, ""

def apply_guess(state: Dict, ch: str) -> bool:
    secret = state["secret"]
    matched = False
    state["guessed"].add(ch)
    for i, s in enumerate(secret):
        if s == ch:
            state["display"][i] = ch
            matched = True
    if not matched:
        state["wrong_guesses"] += 1
    return matched

def is_won(state: Dict) -> bool:
    return '_' not in state["display"]

def is_lost(state: Dict) -> bool:
    return state["wrong_guesses"] >= state["max_tries"]

def render_display(state: Dict) -> str:
    return ' '.join(state["display"])

def render_summary(state: Dict) -> str:
    return f"Secret: {state['secret']} | Guessed: {sorted(list(state['guessed']))} | Wrong: {state['wrong_guesses']}/{state['max_tries']}"