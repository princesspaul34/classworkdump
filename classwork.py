task1 = "number guessing game"
import random

random_number = random.randint(1, 20)
attempts = 0

print("Guess a number from 1 to 20.")

while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == random_number:
        print("You won!")
        break
    elif guess < random_number:
        print("The number is too low.")
    else:
        print("The number is too high.")
else:
    print("You have used all your attempts. You lost.")



task2 = "password validation"
# Ask the user to enter a password. Continue prompting until they enter a valid password.
# Criteria:
# - at least 8 characters long
# - at least one digit
# - at least one uppercase letter

while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        print("Please try again.")
        continue

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        print("Please try again.")
        continue

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        print("Please try again.")
        continue

    print("Valid password.")
    break