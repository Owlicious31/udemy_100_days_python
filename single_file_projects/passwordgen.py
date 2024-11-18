import random
letters = ["a","b","c","d","e","f","g","h","i",
           "j","k","l","m","n","o","p","q","r","s",
           "t","u","v","w","x","y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","%","$","&","*","+"]

print("PASSWORD GENERATOR")
letter_nr = int(input("How many letters do you want? "))
number_nr = int(input("How many numbers you you want? "))
symbol_nr = int(input("How many symbols do you want? "))
sequence_choice = input("Would you like the order of characters "
                        "randomized or not? ").lower()

letter_seg = ""
for letter in letters and range(0, letter_nr):
    letter_seg += random.choice(letters)

number_seg = ""
for number in numbers and range(0, number_nr):
    number_seg += random.choice(numbers)

symbol_seg = ""
for symbol in symbols and range(0, symbol_nr):
    symbol_seg += random.choice(symbols)

if sequence_choice == "yes":
    segments = []
    characters = symbol_seg+letter_seg+number_seg
    for character in characters:
        segments.append(random.choice(characters))
    pass_length = len(characters)
    password = ""
    for segment in segments:
        password += str(segment)
    print(password)
else:
    print(letter_seg+number_seg+symbol_seg)
