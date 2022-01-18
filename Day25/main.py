import pandas

datas=pandas.read_csv("/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day 25/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
data=datas['Primary Fur Color'].unique()
count=[]
# for i in data:
#     if i=="nan":
#         pass
#     else:
#          count.append(len(datas[datas['Primary Fur Color'] == i]))
#  data.to_csv("/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day 25/new_datas.csv")
