import random
from art import logo, vs
from game_data import data
import os

def print_account(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {print_account(account_a)}")

    print(vs)

    print(f"Against B: {print_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper().strip()

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    os.system("cls")

    if is_correct:
        score += 1
        print(logo)
        print(f"You're right!, Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
