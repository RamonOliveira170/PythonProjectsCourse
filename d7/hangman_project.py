import random

word_list = ["pizza", "pajama", "milkshake", "fluffiness", "glyph", "unknown", "wyvern"]

choosen_word = word_list[random.randint(0, len(word_list) - 1)]
# choosen_word = random.choice(word_list)

user_word = ""

"""print(choosen_word)

length_word = len(choosen_word)

print("*" * length_word)

if user_guess[0] in choosen_word:
    print("Yes")
else:
    print("No")
"""

display = []
word_length = len(choosen_word)
for _ in range(word_length):
    display += "_"

user_lives = 6
end_of_game = False
wrong_words = []

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''                                                    
               _
              | |                                            
  +---+       | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  |   |       | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
      |       | | | | (_| | | | | (_| | | | | | | (_| | | | |
      |       |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
      |                            _/ |                      
      |                           |___/         
=========
''']

while not end_of_game:
    print(stages[user_lives])
    print(display)
    print("wrong words:", wrong_words, "\n")
    user_guess = input("Guess a letter: ").lower()
    user_guess = user_guess[0]
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == user_guess:
            display[position] = letter
    
    if user_guess not in choosen_word:
        user_lives -= 1
        wrong_words += user_guess
        print(stages[user_lives])
        if user_lives == 0:
                print("You lose! the word was:", choosen_word)
                end_of_game = True

    if "_" not in display:
        print(display)
        print("You win!")
        if user_lives == 6:
            print("6 lives remaining, well done!")
        end_of_game = True