from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(function, original_text, shift_amount):
    """Encrypts or decrypts text using the caesar cipher
    depending on user input."""
    cipher_text = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {function}d text:\n{cipher_text}")

is_playing = True

while is_playing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text, shift)

    repeat = input("Would you like to go again?(Yes or No)\n").lower()
    if repeat == "no":
        is_playing = False