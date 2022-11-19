import math

numberofStudents, totalMarks, studentName, studentAge, studentGrade, studentMarks = 5, 450, [], [], [], []

for student in range(1, numberofStudents):

    global name, age, grade, obtainedMarks

    print('-------------------------------')
#    name = input('Enter Your Name: ')
    name = 'farhan'
#    age = int(input('Enter Your Age: '))
    age = 18
#    grade = input('Enter Your Class: ')
    grade = 12
    obtainedMarks = int(input('Enter Your Marks: '))
    print('-------------------------------')
    studentName.append(name)
    studentAge.append(age)
    studentGrade.append(grade)
    studentMarks.append(obtainedMarks)
print(studentName, studentAge, studentGrade, studentMarks)


def results():
    return print(f'Student Name: {studentName[index]}\nStudent Age: {studentAge[index]}\nStudent Grade: {studentGrade[index]}\nObtained Marks: {studentMarks[index]}\nTotal Marks: {totalMarks}\nPercentage: {math.floor((studentMarks[index]/totalMarks)*100)}%\nComment: Congrats! You Got First Position!!')


if studentMarks[0] > (studentMarks[1] and studentMarks[2] and studentMarks[3]):
    index = 0
    results()
elif studentMarks[1] > (studentMarks[0] and studentMarks[2] and studentMarks[3]):
    index = 1
    results()

elif studentMarks[2] > (studentMarks[1] and studentMarks[0] and studentMarks[3]):
    index = 2
    results()

else:
    index = 3
    results()
