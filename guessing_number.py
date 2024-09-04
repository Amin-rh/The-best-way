import random


def Guess_Number():
    Lower_Bound = 1
    Upper_Bound = 100

    Number = random.randint(Lower_Bound, Upper_Bound)

    print(f"Guess a number between {Lower_Bound}, {Upper_Bound}.")

    Attempts = 0
    while True:
        try:
            guess = int(input("Enter your number : "))
            Attempts += 1

            if guess < Number:
                print("\tYour guess is too low. try again.")
            elif guess > Number:
                print("\tYour guess is too high. try again.")
            else:
                print(f"\tCongratulation. The correct number was {
                      Number} and you guessed it in {Attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")


Guess_Number()
