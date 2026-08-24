#Append to an existing file
#Create notes.txt containing some text. Take a new sentence from the user and append it to the existing file using "a" mode. Then read and display the complete file.
with open("Q1/notes.txt","w") as file:
    file.write("This is the original text.\n")

sentence = input("Enter a new sentence: ")

with open("Q1/notes.txt","a") as file:
    file.write(sentence + "\n")

with open("Q1/notes.txt", "r") as file:
    print(file.read())