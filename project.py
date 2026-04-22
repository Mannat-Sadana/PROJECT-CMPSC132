import random
def get_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    while True:
        choice=input("Enter 1, 2, or 3: ")
        if choice=="1":
            return "Easy",50
        elif choice=="2":
            return "Medium",100
        elif choice=="3":
            return "Hard",200
        else:
            print("Invalid choice. Please try again.")
def play_game():
    level,high=get_difficulty()
    random_num=random.randint(1,high)
    attempts=0
    print(f"\nYou chose {level} mode.")
    print(f"Guess a number between 1 and {high}.")
    while True:
        guess=input(f"Enter your guess between 1 and {high}: ")
        if guess.isdigit():
            guess=int(guess)
            attempts+=1
            if guess<random_num:
                print("Too low.")
            elif guess>random_num:
                print("Too high.")
            else:
                print("Congratulations! You guessed the correct number!")
                print(f"You guessed it in {attempts} attempts.")
                break
        else:
            print("Invalid input. Please enter a number.")
