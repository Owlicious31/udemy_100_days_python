import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
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
  +---+
  |   |
      |
      |
      |
      |
=========
''']

correct_letters = []
def check_answer(answer, usr_guess):
    display = ""
    for letter in answer:
        if letter == usr_guess:
            display += letter
            correct_letters.append(usr_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    return display

game_over = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

def generate_placeholder():
    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print(placeholder)

generate_placeholder()

while not game_over:
    guess = input("Guess a letter: ").lower()
    final_display = check_answer(chosen_word, guess)
    print(final_display)

    if guess not in chosen_word:
        lives -= 1

    if "_" not in final_display:
        game_over = True
        print("You win.")

    if lives == 0:
        game_over = True
        print("You ran out of lives.")

    print(stages[lives])
