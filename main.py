PLACEHOLDER = "[name]"

# Read all names
with open("./Input/Names/invited_names.txt") as names_file:
    stripped_name = [name.strip() for name in names_file]

# Load the letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

    # Create a letter for each name
    for name in stripped_name:
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", "w") as new_letter_content:
            new_letter_content.write(new_letter)