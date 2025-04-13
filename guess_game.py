import random

score = 0
rounds = 3

print("Welcome to the Guessing Game!")
print(f"You have {rounds} rounds.\n")

for i in range(rounds):
    number = random.randint(1, 10)
    guess = int(input(f"Round {i+1} - Guess a number (1-10): "))

    if guess == number:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The number was {number}.")

print(f"\nGame Over! Your total score is: {score}")
