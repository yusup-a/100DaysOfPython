import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempt = 10
    print(f"You have {attempt} attempts remaining to guess the number.")
elif difficulty == "hard":
    attempt = 5
    print(f"You have {attempt} attempts remaining to guess the number.")

guessed = False
num = random.randint(1,100)

while not guessed:
    if attempt == 0:
        print("You’ve run out of guesses, you lose.")
        break
    guess = int(input("Make a guess: "))
    if guess == num:
        guessed = True
        print(f"You got it! The answer was {num}.")
    elif guess > num:
        attempt -= 1
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")
    elif guess < num:
        attempt -= 1
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempt} attempts remaining to guess the number.")