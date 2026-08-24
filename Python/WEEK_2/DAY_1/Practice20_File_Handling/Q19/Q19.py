#Create a simple student record program that asks for name, age, and marks, writes them to student.txt, and then reads the file and displays the information.
name = input("Enter name: ")
age = input("Enter age: ")
marks = input("Enter marks: ")

file = open("Q19/student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Marks: " + marks + "\n")

file.close()

file = open("Q19/student.txt", "r")

for line in file:
    print(line, end="")

file.close()