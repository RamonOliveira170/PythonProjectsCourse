import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user < 0 or user > 2:
    print("You choose a invalid number! You lose")
else:
    print("Your choice")
    print(game_images[user])

    CPU_choice = random.randint(0, 2)
    print("Computer choice")
    print(game_images[CPU_choice])



    if user == CPU_choice:
        print("Draw!")

    elif user == 0 and CPU_choice == 2:
        print("You win!")

    elif user == 2 and CPU_choice == 0:
        print("You lose")

    elif user > CPU_choice:
        print("You win!")

    elif user < CPU_choice:
        print("You lose")
