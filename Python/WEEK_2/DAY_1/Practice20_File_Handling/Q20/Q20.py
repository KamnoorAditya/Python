#Create a program that:Takes 5 student names from the user.
#Writes them to a file.
#Reads the file using a for loop.
#Prints each student with a serial number.
file = open("Q20/students.txt", "w")

for i in range(5):
    name = input("Enter student name: ")
    file.write(name + "\n")

file.close()

file = open("Q20/students.txt", "r")

count = 1

for name in file:
    print(count, name, end="")
    count += 1

file.close()

