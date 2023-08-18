import pandas as pd
import pyjokes
from pandas import DataFrame as df

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    import random

    return random.choice(reactions)


def print_random_joke_and_reaction():
    print("\n" + pyjokes.get_joke() + "\n")
    print(get_random_reaction() + "\n")


if __name__ == "__main__":
    print_random_joke_and_reaction()
