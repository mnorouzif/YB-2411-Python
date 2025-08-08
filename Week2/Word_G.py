import random
import string


def get_random_word():
    """Return a random word from a small built-in list."""
    words = [
        "python", "variable", "function", "iterator", "notebook",
        "pipeline", "dataset", "computer", "research", "analytics"
    ]
    return random.choice(words)

def make_blanks(word):
    """Create the initial blanks list for the secret word."""
    return ["_" for _ in word]

def prompt_for_letter(used_letters):
    """
    Ask the user for a single alphabetic letter that hasn't been used.
    Returns the lowercase letter.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print(" → Please enter a single A-Z letter.")
            continue
        if guess in used_letters:
            print(" → You already tried that letter.")
            continue
        return guess

def reveal_letters(word, blanks, letter):
    """
    Replace matching blanks with the guessed letter.
    Returns True if at least one letter was revealed; otherwise False.
    """
    found_any = False
    for i, ch in enumerate(word):
        if ch == letter and blanks[i] == "_":
            blanks[i] = letter
            found_any = True
    return found_any

def all_blanks_filled(blanks):
    """Check win condition."""
    return "_" not in blanks

def play_game(max_lives=6):
    """Main game loop following the provided algorithm."""
    secret = get_random_word()
    blanks = make_blanks(secret)
    lives = max_lives
    used = set()

    print("\nWelcome to Word Guessing!")
    print(f"The word has {len(secret)} letters.")
    print(" ".join(blanks))

    while True:
        # Ask the user to guess a letter
        guess = prompt_for_letter(used)
        used.add(guess)

        # Is the guessed letter in the word?
        if reveal_letters(secret, blanks, guess):
            print("\n Well done, Nice job! You found a letter.")
            print(" ".join(blanks))
            # Are all blanks filled?
            if all_blanks_filled(blanks):
                print("\n Congratulation! You guessed the word!")
                print(f"Word: {secret}")
                print("GAME OVER")
                break
        else:
            # Lose a life
            lives -= 1
            print(f"\nNope. You lose a life. Lives left: {lives}")
            print(" ".join(blanks))

            # Have they run out of lives?
            if lives <= 0:
                print("\n Out of lives & Sad story!")
                print(f"The word was: {secret}")
                print("GAME OVER")
                break

        # (loop continues to ask for another letter)

# --- Run the game project ------------------------------------------------------------
if __name__ == "__main__":
    play_game()
