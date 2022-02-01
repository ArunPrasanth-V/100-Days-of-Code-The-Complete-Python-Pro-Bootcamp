
# import random
# name=["arun","john","vimal","kishore"]
# new_dict={item:random.randint(1,100) for item in name}
# print(new_dict)
# pass_student={item:new_dict.get(item) for item in new_dict if new_dict.get(item)>60}
# print(pass_student)

# sentance="what is the air speed velocity of an unloaden"
# new_dictionary={i:len(i) for i in sentance.split() }
# print(new_dictionary)

weather_c={
    "monday":12,
    "tuesday":14,
    "wednesday":15,
    "thursday":14,
    "friday":21,
    "saturday":22,
    "sunday":24
}
new_weather_f={day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
print(new_weather_f)
