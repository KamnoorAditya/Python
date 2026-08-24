#Ask the user for a filename. Check whether the file exists before attempting to open it. Display an appropriate message depending on whether the file exists or not.
import os

filename = input("Enter filename: ")

if os.path.exists(filename):
    print("File exists.")
else:
    print("File does not exist.")
