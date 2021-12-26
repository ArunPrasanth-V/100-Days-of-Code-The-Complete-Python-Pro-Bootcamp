visited=[
         {
             "countary":"Canada",
             "city":["Toronto","Ontario","ottawa"],
             "visited":0
         },
         {
             "countary":"USA",
             "city":["NewYork","Ontario","ottawa"],
             "visited":0
         }
       ]

def insert(country,visitedtime,city):
    new_record={}
    new_record["country"]=country
    new_record["visited"]=visitedtime
    new_record["city"]=city
    visited.append(new_record)

country="India"
visitedtime=5
city=["Salem","trichy","perambalur"]
insert(country,visitedtime,city)
print(visited)
