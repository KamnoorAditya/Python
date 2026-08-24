# Ask the user for a filename and delete that file. If the file doesn't exist, display an appropriate message instead of allowing the program to crash.
import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    os.remove(filename)
    print("File deleted.")
else:
    print("File does not exist.")