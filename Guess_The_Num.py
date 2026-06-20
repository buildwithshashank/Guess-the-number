import random

number = random.randint(0, 100)
guesses = 0

while True:
    guess = int(input("Guess a number: "))
    guesses = guesses + 1

    if guess < number:
        print("Higher")

    elif guess > number:
        print("Lower")

    else:
        print("Correct! Total Tries = ",guesses)

        break

    