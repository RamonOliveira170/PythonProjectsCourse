import random

print("Heads or Tails?")
user = input("Your choice: ").capitalize()

heads_tails = random.randint(0, 1)

if heads_tails == 0:
    heads_tails = "Heads"
else:
    heads_tails = "Tails"

if user == heads_tails:
    print(f"{user}! you won!")
else:
    print(f"{heads_tails}! you lose!")
