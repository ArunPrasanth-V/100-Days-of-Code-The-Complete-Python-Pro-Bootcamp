# import csv
#
# with open('/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day 25/weather_data.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)
# temprature=[]
# for i in data:
#     if(i[1]=="temp"):
#         pass
#     else:
#         temprature.append(int(i[1]))
# print(temprature)

import pandas
datas=pandas.read_csv("/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day 25/weather_data.csv")
# print(datas)
# print(datas["temp"])
datas_dicts=datas.to_dict()
# print(datas_dicts)

# print(datas["temp"].to_list())

#calculate average temprature = sumof mesured temp/no.of mesurement


# print(sum(datas_list)/len(datas_list))

# in panda library method called mean
# print(datas["temp"].mean())
# print(datas["temp"].max())
# print(datas.condition)

# print(datas[datas.day=="Monday"])
# print(datas[datas.temp==datas.temp.max()])
monday=datas[datas.day=="Monday"]
temprature=int(monday.temp)
print(temprature*9/5+32)
