alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N", "O", 'P', "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alphabet_length = len(alphabet)

#print(letter_list.index("Z"))

def encrypt(text):
    user_keyword = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        #print(letter)
        #user_keyword += letter_list[letter_index + user_space]    
        if (letter_index + shift) >= alphabet_length:
            user_keyword += alphabet[(letter_index + shift) % 26]
        else:
            user_keyword += alphabet[letter_index + shift]
    return f"The encoded text is: {user_keyword}" 

def decrypt(text):
    user_keyword = ""
    for letter in text:
        letter_index = alphabet.index(letter)
        user_keyword += alphabet[(letter_index - shift)]
    return f"The decoded text is: {user_keyword}"


def caesar(text, shift_amount, direction):
    print("Encripting..." if direction[0] == "D" else "Decripting...")
    end_text = ""
    if direction[0] == "D":
            shift_amount *= -1 # 5 *- 1 = -5
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    return f"Result: {end_text}"

again = True

while again == True:
    user_text = input("Type your message: ").upper()

    shift = int(input("Shift number: "))

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt': ").capitalize()

    """if direction[0] == "E":
        print("Encripting...")
        print(encrypt(user_word))

    elif direction[0] == "D":
        print("Decripting...")
        print(decrypt(user_word))"""
    
    print(caesar(user_text, shift, direction))

    stop = input("Type 'Yes' if you want to go again. Otherwise type 'no': ").capitalize()
    
    if stop[0] != "Y":
        again = False

print("Goodbye!")

