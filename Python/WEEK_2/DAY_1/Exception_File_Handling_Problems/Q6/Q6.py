# Ask the user for a filename and create it using "x" mode. If a file with the same name already exists, handle the situation appropriately.
filename = input("Enter filename: ")

try:
    with open(filename, "x") as file:
        file.write("New file created.")

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")