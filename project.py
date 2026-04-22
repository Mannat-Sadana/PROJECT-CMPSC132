import random
def main():
    random_num=random.randint(1,100)
    attempts=0
    print("Welcome to the Number Guessing Game!")
    while True:
        guess=input("Enter your guess between 1 and 100: ")
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
main()