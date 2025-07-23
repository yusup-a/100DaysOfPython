# # # with open("weather_data.csv") as file:
# # #     data_lines = file.readlines()
# # #
# # # print(data_lines)
# #
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     print(data)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
#
# print(data["temp"].mean())
# max_temp = data["temp"].max()
# print(max_temp)
#
# print(data["condition"])
# print(data.condition)
#
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == max_temp])
#
# monday = data[data["day"] == "Monday"]
# #monday.temp[index number of the row you are working on]
# monday_temp = monday["temp"][0]
# fahrenheit = (monday_temp * 9 / 5) + 32
# print(fahrenheit)
#
# dictio = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_dict = pandas.DataFrame(dictio)
# print(data_dict)
# data_dict.to_csv("new_data.csv")
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250531.csv")

colors = data["Primary Fur Color"]


grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])


# for color in colors:
#     if color == "Cinnamon":
#         red += 1
#     elif color == "Gray":
#         grey += 1
#     elif color == "Black":
#         black += 1

colors_dict = {
    "Fur Color" : ["grey", "red", "black"],
    "Count": [grey, red, black]
}

data2 = pandas.DataFrame(colors_dict)
data2.to_csv("squirrel_count.csv")

print(data2)