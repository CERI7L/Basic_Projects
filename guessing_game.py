import random


def guesses(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry, that's too low")
        if guess > random_number:
            print("sorry, that's too high")

    print("That's correct!")


guesses(10)

