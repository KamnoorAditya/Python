# Ask the user for a filename and attempt to open it in read mode. Handle the situation where:
#The file doesn't exist.
#Another unexpected error occurs
filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")

except Exception as e:
    print("An unexpected error occurred:", e)
