import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for (index, row) in data.iterrows()}


# for (index, row) in data.iterrows():
#     data_dic[row.letter] = row.code
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def get_user_input():
    user_input = input("Please, enter the word which you can't pronounce \n")
    input_list = [char.upper() for char in user_input]
    return input_list
# user_input_frame = {item: key for (item, key) in data_dic.items() if item in user_input_list}
# result = list(user_input_frame.values())


is_data_valid = False
while not is_data_valid:
    user_input_list = get_user_input()
    try:
        result = [data_dic[char] for char in user_input_list]
        print(result)
        is_data_valid = True
    except KeyError:
        print("Sorry, but only letter allowed in alphabet")
        pass





