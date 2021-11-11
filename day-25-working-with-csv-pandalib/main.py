# How to read CSV file using open method
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)
# Working with CSV file using internal method
# import csv
#
# with open("weather_data.csv") as dat_file:
#     data = csv.reader(dat_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

average = data["temp"].mean()
print(f"The average temp is {average} degree by C")

max_temp = data["temp"].max()
print(f"Max temp in a week is a {max_temp}")

# Get data in column
print(data["condition"])
print(data.condition)

# Get data in a row
print(data[data.day == "Monday"])
print(data[data.temp == max_temp])

# Working with row
monday = data[data.day == "Monday"]
print(monday.temp)
monday.temp = 53.6
print(monday.temp)

# Create a data from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")
