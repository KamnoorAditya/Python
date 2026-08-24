#Overwrite an existing file
#Create a file containing some old information. Ask the user for new information and use "w" mode to replace the old content completely. Read the file afterward to verify the change.
with open("Q1/info.txt", "w") as file:
    file.write("This is old information.")

new_info = input("Enter new information: ")

with open("Q1/info.txt", "w") as file:
    file.write(new_info)

with open("Q1/info.txt", "r") as file:
    print("Updated content:")
    print(file.read())