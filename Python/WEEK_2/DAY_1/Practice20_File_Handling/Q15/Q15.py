#Create a file containing:
#Rahul 80
#man 35
#Priya 92
#Neha 45
#Read the file and print only students who scored 50 or above.
file = open("Q15/students.txt", "w")

file.write("""Rahul 80
Man 35
Priya 92
Neha 45""")

file.close()


file = open("students.txt", "r")

students = {}

for line in file:
    name, marks = line.split()
    students[name] = int(marks)

file.close()

for name in students:
    if students[name] >= 50:
        print(name, students[name])