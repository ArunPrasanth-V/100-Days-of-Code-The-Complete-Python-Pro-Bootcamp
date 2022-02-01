list = ["a","b","arun","vimal","remote job"]

# Before list comprehension
# new_list1 = []
# for i in list:
#     new_list1.append(i)


# # After List Comprehension
# new_list2 = [i.upper() for i in list if len(i)>3]
# print(new_list2)
#
#
#
# # Square root of the number
# import math
#
# number=[1,1,2,3,5,8,21,34,55]
# new_list3=[i*i for i in number ]
# print(new_list3)
#
#
# #even number
# new_list4=[i for i in number if i%2==0]
# print(new_list4)

# Reading a text file and print if the number contains both list.


with open('/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day26/file1.txt') as f:
    file1_data=f.readlines()
with open('/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day26/file2') as f1:
    file2_data=f1.readlines()

result=[int(i) for i in file1_data if i in file2_data]
print(result)


