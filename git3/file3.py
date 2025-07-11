import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100.")

while True:
    guess = input("Enter your guess (or 'exit' to quit): ")
    if guess.lower() == 'exit':
        print("Game exited. The number was:", number)
        break

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break

