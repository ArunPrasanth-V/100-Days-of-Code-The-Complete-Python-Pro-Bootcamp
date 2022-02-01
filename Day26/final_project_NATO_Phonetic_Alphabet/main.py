import pandas

name=input("Enter Your Name : ").upper()
list=pandas.read_csv("/home/javapogrammer/PycharmProjects/bootcampfrom22thday/Day26/final_project_NATO_Phonetic_Alphabet/Phonetic_alphabet.csv")
phonetic_dict={row.letter: row.code for(index, row)in list.iterrows()}
output_list=[phonetic_dict[letter] for letter in name]
print(output_list)
