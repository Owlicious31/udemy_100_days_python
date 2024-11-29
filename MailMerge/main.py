PLACEHOLDER = "[name]"

def mail_merge():
    with open("./Input/Names/invited_names.txt") as name_file:
        names = name_file.readlines()

    for name in names:
        name = name.strip("\n")
        with open("./Input/Letters/starting_letter.txt") as letter_file:
            new_letter = letter_file.read()
            new_letter = new_letter.replace(PLACEHOLDER,name)

        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode= "w") as completed_letter_file:
            completed_letter_file.write(new_letter)

if __name__ == "__main__":
    mail_merge()
