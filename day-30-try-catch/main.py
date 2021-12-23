# File Not Fond

# Using try block to try execute the part of code
try:
    file = open("a_file.txt")
    a_dic = {"key": "value"}
    # print(a_dic["another_key"])
    print(a_dic["key"])
# Block except will be executed in case if block try shows and error, we should not use block except without
# pointing on what kind of error we are going to catch, in other case try block will be ignored in case of any error
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
# We are able to have few except block for different error types
# We also can interpret the error message as variable
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
# Else block will be executed in case if try block will have no errors
# like what else are you going to do?
# If try will not be execute, the else block will never be triggered
else:
    content = file.read()
    print(content)
# Block finally is going to run no matter what happens
finally:
    file.close()
    print("file was closed.")
    if a_dic["key"] == "value":
        # We also able to raise our own error or exception using block raise
        raise ValueError("invalid a_dic value")