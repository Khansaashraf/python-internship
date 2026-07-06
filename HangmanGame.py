import random

# Predefined list of words and hints for the Hangman game
WORDS = [
    {"word": "python",  "hint": "A popular programming language"},
    {"word": "jungle",  "hint": "A dense tropical forest"},
    {"word": "planet",  "hint": "Earth is one of these"},
    {"word": "bridge",  "hint": "Connects two sides of a river"},
    {"word": "music",   "hint": "Art made of sound and rhythm"},
]

#hangman stages for visual representation of the game

HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
           |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ==========""",
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ==========""",
]

MAX_WRONG = 6


def display_state(secret, guessed, wrong):
    print(HANGMAN_STAGES[len(wrong)])
    print()

    # Word display: revealed letters or underscores
    display = " ".join(c.upper() if c in guessed else "_" for c in secret)
    print(f"  Word: {display}")
    print()

    if wrong:
        print(f"  Wrong guesses ({len(wrong)}/{MAX_WRONG}): {', '.join(c.upper() for c in sorted(wrong))}")
    else:
        print(f"  Wrong guesses: none yet")
    print()


def play_game():
    # pick a random word from hints
    pick = random.choice(WORDS)
    secret = pick["word"]
    hint = pick["hint"]
    guessed = set() #correct gusses
    wrong = [] #wrong gusses

    print("\n" + "=" * 40)
    print("         HANGMAN")
    print("=" * 40)
    print(f"  Hint: {hint}")
    print(f"  The word has {len(secret)} letters.")

    while True: #while loops keep it running until the user either wins or loses.
        display_state(secret, guessed, wrong)

        # Check win
        if all(c in guessed for c in secret):
            print(f"  You won! The word was: {secret.upper()}")
            break

        # Check loss
        if len(wrong) >= MAX_WRONG:
            print(f"  Game over! The word was: {secret.upper()}")
            break

        # Get input
        raw = input("  Guess a letter: ").strip().lower()

        if len(raw) != 1 or not raw.isalpha():
            print("  Please enter a single letter.")
            continue

        if raw in guessed or raw in wrong:
            print(f"  You already guessed '{raw.upper()}'. Try another.")
            continue

        if raw in secret:
            guessed.add(raw)
            print(f"  '{raw.upper()}' is in the word!")
        else:
            wrong.append(raw)
            remaining = MAX_WRONG - len(wrong)
            print(f"  '{raw.upper()}' is not in the word. {remaining} guess{'es' if remaining != 1 else ''} remaining.")


def main():
    while True:
        play_game()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing!\n")
            break


if __name__ == "__main__":
    main()