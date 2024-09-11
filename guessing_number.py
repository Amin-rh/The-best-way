import random


def Guess_Number():
    # Specify range of numbers
    _Lower_Bound = 1
    _Upper_Bound = 100

    # Generating numbers
    _Number = random.randint(_Lower_Bound, _Upper_Bound)

    print(f"Guess a number between {_Lower_Bound}, {_Upper_Bound}.")

    _Attempts = 0
    while True:
        try:
            Guess = int(input("Enter your number : "))
            _Attempts += 1

            if Guess < _Number:
                print("\tYour guess is too low. try again.")
            elif Guess > _Number:
                print("\tYour guess is too high. try again.")
            else:
                print(f"\tCongratulation. The correct number was {
                      _Number} and you guessed it in {_Attempts} attempts.")
                break
        # Handling value error
        except ValueError:
            print("\tPlease enter a valid integer.")


Guess_Number()
