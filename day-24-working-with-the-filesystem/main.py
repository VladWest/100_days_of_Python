# Small tutorial how to write and read into file from Python

# Open file and read a content
# var_file is something like variable
with open("text.txt", mode="r") as read_file:
    content = read_file.read()
    print(content)
# Write to the file without overwriting data using mode a for open method
with open("text.txt", mode="a") as append_to_file:
    append_to_file.write("\nJust a simple new line")

# Reading files as method, using open
file = open("text.txt", mode="r")
content_1 = file.read()
file.close()

# Writing to the file with overwriting(possible to create new file if not exist)
# Using mode w with open method
with open("new_text_file.txt", mode="w") as aggressive_write_file:
    aggressive_write_file.write("Here you will see only this message.")
