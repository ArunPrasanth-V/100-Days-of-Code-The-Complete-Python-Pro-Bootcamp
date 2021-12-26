
Student_score={"Viaml":90,
                "Arun":90,
                "rahim":70,
                "neha":50}
Student_grade={}
for i in Student_score:
    print(Student_score[i])
    if Student_score[i]>90:
        Student_grade[i]="Outstanding"
    elif Student_score[i]>80:
        Student_grade[i]="Exceed Expectation"
    elif Student_score[i]>70:
        Student_grade[i]= "Acceptable"
    else :
        Student_grade[i] = "Of Fine "

print(Student_grade)
