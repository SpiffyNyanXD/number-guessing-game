"""Number Guessing Game module."""

import random


def get_integer(prompt, min_value=None, max_value=None):
    """Get a valid integer from the user with optional range checking."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Enter a number >= {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Enter a number <= {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a whole number.")


def choose_difficulty():
    """Prompt the user to choose a difficulty level."""
    print("\nChoose difficulty:")
    print("1. Easy   (1-20, 7 attempts)")
    print("2. Medium (1-50, 8 attempts)")
    print("3. Hard   (1-100, 10 attempts)")

    choice = get_integer("Enter 1, 2, or 3: ", 1, 3)

    if choice == 1:
        return 20, 7
    if choice == 2:
        return 50, 8
    return 100, 10


def play_game():
    """Play one round of the Number Guessing Game."""
    print("Welcome to the Number Guessing Game!")

    max_number, max_attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts = 0
    score = 100

    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        guess = get_integer(
            f"Attempt {attempts + 1}. Take a guess: ", 1, max_number
        )
        attempts += 1

        if guess < secret_number:
            print("Too low.")
            difference = secret_number - guess
            if difference > max_number // 2:
                print("Hint: You're far off.")
            else:
                print("Hint: You're close.")
            score -= 10

        elif guess > secret_number:
            print("Too high.")
            difference = guess - secret_number
            if difference > max_number // 2:
                print("Hint: You're far off.")
            else:
                print("Hint: You're close.")
            score -= 10

        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            print(f"Your score: {max(score, 0)}")
            return

    print(f"\nGame over. The number was {secret_number}.")
    print("Your final score: 0")


def main():
    """Main loop for the game."""
    while True:
        try:
            play_game()

            again = input("\nPlay again? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("Thanks for playing.")
                break
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing.")
            break


if __name__ == "__main__":
    main()
