import random
from art import logo

def guess_number(difficulty):
    computer_number = random.randint(1, 100)
    if difficulty == "Easy":
        user_attempts = 10
    else:
        user_attempts = 5

    user_number = 0
    while user_attempts > 0:
        print(f"You have {user_attempts} remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        if user_number > computer_number:
            print("Too high.")
            user_attempts -= 1
        elif user_number < computer_number:
            print("Too low.")
            user_attempts -= 1
        else:
            print(f"You guessed it right '{user_number}'!")
            return 
    
    print("You've run out of guesses, you lose")
    print(f"The number was {computer_number}")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Type 'easy' or 'hard': ").capitalize().strip()    

if difficulty == "Easy" or difficulty == "Hard":
    guess_number(difficulty)
else:
    print("Invalid Difficulty.")
