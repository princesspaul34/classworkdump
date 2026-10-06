#number guessing game
#write a program where the computer selects a random number between 1 and 20. the user has 5 attemps to guess the correct number. provide feedback for each guess (too high, too low, correct). if the user guesses correctly within 5 attempts, print "Congratulations! You guessed the number." otherwise, print "Sorry, you've used all your attempts. The correct number was [number]."
import random

number = random.randint(1, 20)
attempts = 5

for i in range(attempts):
    guess = int(input("Guess a number between 1 and 20: "))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Sorry, you've used all your attempts. The correct number was {number}.")

#ask the user to enter a passsword.continue prompting until password:
#is at least one digit
#is at least one uppercase letter
#is at least 8 characters long
while True:
    password = input("Enter a password: ")
    if (any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        len(password) >= 8):
        print("Password accepted.")
        break
    else:
        print("Password must be at least 8 characters long, contain at least one digit, and one uppercase letter. Please try again.")

#create a menu-driven ATM interface where the user can:
#withdraw money
#deposit money
#check balance
#exit the program
name = input("Enter your name: ")
password = input("Enter a password:")
balance = 1000  # initial balance
while True:
    print("\nATM Menu:")
    print("1. Withdraw Money")
    print("2. Deposit Money")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        withdraw = int(input("Enter the amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw
            print(f"Withdrawal successful. Your new balance is {balance}.")
    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: "))
        balance += deposit
        print(f"Deposit successful. Your new balance is {balance}.")
    elif choice == "3":
        print(f"Your current balance is {balance}.")
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")

# Multiply the two variables and store the result in a new variable called product. Print the result.
product = 5 * 10
print(f"The product is {product}.")

# Divide x by y and print the result.
x = 20
y = 4
result = x / y
print(f"The result of dividing {x} by {y} is {result}.")

# Create a variable age and let user assign age. Check if the age is greater than or equal to 18 and print the result
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")

# Create two variables math_score and english_score, each with values between 0 and 100. Check if both are above 50 and print True or False.
math_score = int(input("Enter your math score: "))
english_score = int(input("Enter your English score: "))
if math_score > 50 and english_score > 50:
    print(True)
else:
    print(False)

# Create a variable is_logged_in and set it to True. Use a logical NOT to print the opposite value.
is_logged_in = True
print(not is_logged_in)

# Declare a variable is_raining as True and has_umbrella as False. Use logical OR to determine if you can go outside and print the result.
is_raining = True
has_umbrella = False
if not is_raining or has_umbrella:
    print("You can go outside.")
else:
    print("You cannot go outside.")

# Create a variable number and assign any integer. Check if the number is even using the modulo operator and print True or False.
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(True)
else:
    print(False)