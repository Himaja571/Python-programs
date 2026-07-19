import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess < secret:
        print("Too Low!")
    elif guess > secret:
        print("Too High!")
    else:
        print("Congratulations! You guessed correctly.")
        break