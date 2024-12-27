import random


def guess(x):
    random_number = random.randrange(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a random number between 1 and {x}:'))
        if guess < random_number: \
                print("sorry , guess again it's too low. ")
        elif guess > random_number: \
                print("sorry , guess again it's to high.")

    print(f" \U0001F37E congrats you guessed the number {random_number} is correct \U0001F37E ")


guess(10)
