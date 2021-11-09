# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
file_name = open("Input/Names/invited_names.txt")
names = file_name.readlines()
file_name.close()

starting_letter_file = open("Input/Letters/starting_letter.txt")
starting_letter = starting_letter_file.read()
starting_letter_file.close()

for name in names:
    new_name = name.strip("\n")
    letter_name = f"Output/ReadyToSend/Invitation_for_{new_name}"
    # Replace the [name] placeholder with the actual name.
    end_letter = starting_letter.replace("[name]", new_name)
    end_file = open(letter_name, mode="w")
    # Save the letters in the folder "ReadyToSend".
    end_file.write(end_letter)
    end_file.close()

