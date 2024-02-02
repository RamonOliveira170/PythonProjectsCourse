import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

cpu = random.randint(0, 2)

if user == 0:
    print("You choose Rock")
    if cpu == 0:
        print("CPU choose Rock")
        print("Draw!")
    elif cpu == 1:
        print("CPU choose Paper")
        print("You lose")
    elif cpu == 2:
        print("CPU choose Scissors")
        print("You WON!")

if user == 1:
    print("You choose Paper")
    if cpu == 0:
        print("CPU choose Rock")
        print("You WON!")
    elif cpu == 1:
        print("CPU choose Paper")
        print("Draw!")
    elif cpu == 2:
        print("CPU choose Scissors")
        print("You lose")

if user == 2:
    print("You choose Scissors")
    if cpu == 0:
        print("CPU choose Rock")
        print("You lose")
    elif cpu == 1:
        print("CPU choose Paper")
        print("You WON!")
    elif cpu == 2:
        print("CPU choose Scissors")
        print("Draw!")