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