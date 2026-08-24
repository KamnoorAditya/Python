#Append multiple lines
#Create students.txt with 3 student names. Ask the user for 2 additional names and append them to the same file without deleting the existing names.
with open("Q2/students.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Priya\n")
    file.write("Aman\n")

for i in range(2):
    name = input("Enter student name: ")

    with open("Q2/students.txt", "a") as file:
        file.write(name + "\n")

with open("Q2/students.txt", "r") as file:
    print(file.read())