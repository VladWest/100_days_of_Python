import pandas
#Central Park Squirrel Data Analysis - her solution
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_list = fur_color.to_list()
black = 0
gray = 0
red = 0
mixed_color = 0
for color in fur_color_list:
    if color == "Black":
        black += 1
    elif color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        red += 1
    else:
        mixed_color += 1

squirrel_dic = {
    "Fur color": ["Gray", "Red", "Black", "Mixed"],
    "Count": [gray, red, black, mixed_color]
}

new_data = pandas.DataFrame(squirrel_dic)
new_data.to_csv("count_of_squirrel_furs_by_color.csv")
