import pandas

data_dict={
          "student":["arun","varun","vimal"],
          "score":[90,92,95]
          }
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

