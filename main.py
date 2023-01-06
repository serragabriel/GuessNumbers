import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'adivinhe um numero entre 1 e {x}: '))

        if guess == random_number:
            print(f"Parabens voce adivinhou o numero correto '{guess}'")

        elif guess > random_number:
            print("Menos")
        elif guess < random_number:
            print("Mais")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"{guess} <---- muito alto H, muito baixo L e C para numero correto = ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"o computador acertou o seu numero {guess}")


computer_guess(1000)
guess(10)
guess(100)
computer_guess(10000)
