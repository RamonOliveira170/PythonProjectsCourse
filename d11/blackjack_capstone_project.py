import os
import random
from art import logo

def random_card():
    """Returns a random card from the deck"""
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    length_cards = len(cards) - 1
    return cards[random.randint(1, length_cards)]
    #random.choice(cards)

def calculate_blackjack(cards):
    """Calculates the value of the cards in the hand of the players"""
    result = 0
    for card in cards:
        if type(card) is str:
            if card == "A" and result >= 11:
                result += 1
            elif card == "A" and result < 11:
                result += 11
            else:
                result += 10
        else:
            result += card
    return result

def blackjack(user, computer):
    """Compares the values of the cards and show the winner"""
    user_total = calculate_blackjack(user)
    
    #print(user_total)
    
    computer_total = calculate_blackjack(computer)
    
    #print(computer_total)

    pick_card = True
    while pick_card:
        more_cards = input("Type 'y' to get another card, type 'n' to pass: ").capitalize().strip()

        if more_cards == "Y":
            user.append(random_card())
            user_total = calculate_blackjack(user)
            print(f"Your cards: {user}: {user_total}")
            if user_total > 21:
                return "You lose"
        else:
            pick_card = False

    while computer_total < 17:
        computer.append(random_card())
        computer_total = calculate_blackjack(computer)
        print(f"Computer's less than 17 {computer}: {computer_total}")

    print(f"\nYour final hand {user}: {user_total}")
    print(f"Computer's final hand {computer}: {computer_total}")

    if user_total > 21:
        return "You lose"
    elif computer_total > 21:
        return "You win"
    elif user_total > computer_total:
        return "You win"
    elif user_total < computer_total:
        return "You lose"
    else:
        return "draw"

def give_cards(): 
    """Give the cards for the players"""
    print(logo)
    user_cards = []
    user_cards.append(random_card())
    user_cards.append(random_card())
    print(f"Your cards: {user_cards}")

    computer_cards = []
    computer_cards.append(random_card())
    print(f"Computer's first card: {computer_cards}")

    computer_cards.append((random_card()))

    print(blackjack(user_cards, computer_cards))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").capitalize().strip() == "Y":
    os.system("cls")
    give_cards()
