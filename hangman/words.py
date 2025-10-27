import random
from typing import List

def load_words(path: str) -> List[str]:
    with open(path, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def choose_secret_word(words: List[str]) -> str:
    return random.choice(words)
