"""
Number Guessing Game
CMPSC 132 Final Project
 
A single-player terminal-based number guessing game with three difficulty levels, limited attempts, replay support, warmer/colder hints, scoring, and best-score tracking across rounds.
"""
 
import random
 
def get_difficulty():
    """
    Prompt the user to choose a difficulty level.
    Returns a tuple of (level_name, upper_bound, max_tries) based on the user's choice. Keeps re-prompting until a valid choice is entered.
    """
    print("\nChoose difficulty:")
    print("1. Easy   (1-50,  10 tries)")
    print("2. Medium (1-100, 7 tries)")
    print("3. Hard   (1-200, 5 tries)")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "Easy", 50, 10
        elif choice == "2":
            return "Medium", 100, 7
        elif choice == "3":
            return "Hard", 200, 5
        else:
            print("Invalid choice. Please try again.")
 
def get_valid_guess(high):
    """
    Get a valid integer guess from the user between 1 and `high`.
    Re-prompts on non-numeric input or out-of-range values WITHOUT counting them as a wasted attempt. Returns the guess as an int.
    """
    while True:
        user_input = input(f"Enter your guess between 1 and {high}: ").strip()
        if not user_input.isdigit():
            print("Invalid input. Please enter a whole number.")
            continue
        guess = int(user_input)
        if guess < 1 or guess > high:
            print(f"Out of range. Please enter a number between 1 and {high}.")
            continue
        return guess
 
def get_hint(guess, target, high):
    """
    Return a warmer/colder hint based on how close the guess is.
    The threshold scales with difficulty so hints feel fair on every range (5% of the range for "very close", 15% for "warm").
    """
    distance = abs(guess - target)
    very_close = max(2, high * 0.05)
    warm = max(5, high * 0.15)
    if distance <= very_close:
        return "Very close!"
    elif distance <= warm:
        return "Warm."
    else:
        return "Cold."

def calculate_score(tries_used, max_tries, level):
    """
    Calculate a score for a winning round.
    Score rewards efficiency (fewer tries = more points) and difficulty (Hard mode multiplier > Medium > Easy).
    """
    multipliers = {"Easy": 1, "Medium": 2, "Hard": 3}
    tries_remaining = max_tries - tries_used
    return (tries_remaining + 1) * 10 * multipliers[level]

def play_game(best_scores):
    """
    Play one round of the number guessing game.
    Picks a random number based on the chosen difficulty, then loops until the user guesses correctly or runs out of tries. Updates `best_scores` (a dict keyed by difficulty) when a new best is set.
    """
    level, high, max_tries = get_difficulty()
    random_num = random.randint(1, high)
    guess_count = 0
    print(f"\nYou chose {level} mode.")
    print(f"Guess a number between 1 and {high}.")
    print(f"You have {max_tries} tries.")
    while guess_count < max_tries:
        user_guess = get_valid_guess(high)
        guess_count += 1
        if user_guess < random_num:
            print(f"Too low. {get_hint(user_guess, random_num, high)}")
        elif user_guess > random_num:
            print(f"Too high. {get_hint(user_guess, random_num, high)}")
        else:
            score = calculate_score(guess_count, max_tries, level)
            print("Congratulations! You guessed the correct number!")
            print(f"You guessed it in {guess_count} attempts.")
            print(f"Score: {score} points")
            previous_best = best_scores.get(level)
            if previous_best is None or score > previous_best:
                print(f"New best score for {level} mode!")
                best_scores[level] = score
            else:
                print(f"Best score for {level} mode: {previous_best}")
            return
        tries_left = max_tries - guess_count
        if tries_left > 0:
            print(f"Tries left: {tries_left}")
    print(f"Out of tries. The number was {random_num}.")
 
def show_best_scores(best_scores):
    """Display the best score for each difficulty played this session."""
    if not best_scores:
        return
    print("\n--- Best Scores This Session ---")
    for level in ["Easy", "Medium", "Hard"]:
        if level in best_scores:
            print(f"{level}: {best_scores[level]} points")
    print("--------------------------------")
 
 
def main():
    """
    Entry point for the game. Greets the user, tracks best scores across rounds, and supports replay.
    """
    print("Welcome to the Number Guessing Game!")
    best_scores = {}
    while True:
        play_game(best_scores)
        show_best_scores(best_scores)
        again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")