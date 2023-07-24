import random
# Algo
def guess_number(guess_limit, number):
    random_number = random.randint(1, number)

    try:
        while guess_limit > 0 :
            guess = int(input("What is your guess?"))
            guess_limit -=1
            if random_number == guess:
                print("Voilla! you guessed it right")
                exit()
                
            elif guess > number:
                print("Your's guess is too high.")
                print(f"You have {guess_limit} guesse's left.")

            else:
                print("Sorry that was wrong.")
                print(f"You have {guess_limit} guesse's left.")
        print("Game over!")
        print(f"The number was {random_number}")
        try_again()

    except ValueError:
        print("Only Integers are allowed.")
# Levels
def easy():
    print("You are to guess a number between 1 - 10 and you have 6 guesses")
    guess_number(6, 10)

def medium():
    print("You are to guess a number between 1 - 20 and you have 4 guesses")
    guess_number(4, 20)

def hard():
    print("You are to guess a number between 1 - 50 and you have 3 guesses")
    guess_number(3, 50)

# Repeat
def try_again():
    again = input("Do you wnat to play again. Yes/No")

    if again.upper() == 'YES':
        start()
    elif again.upper() == 'NO':
        print("Thanks for playing")
    else:
        print("Try again incoorect input")
        try_again()

# Driver code
def start():
    print("Welcome to the guessing game.")
    difficulty = input("Choose your difficulty between Easy,Medium and Hard.")

    if difficulty.upper() == 'EASY':
        easy()
    elif difficulty.upper() == "MEDIUM":
        medium()
    elif difficulty.upper() == "HARD":
        hard()
    else:
        print("This is wrong input")
        start()
# calling to the start
start()