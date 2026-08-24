#A file contains a student's name, age, and marks on separate lines. Use readline() to read all three values and display them.
file=open("Q6/data.txt","w+")
file.write("""aditya
22
88""")
file.seek(0)
while True:
    line=file.readline()
    if line=="":
        break
    else:
        print(line,end="")
file.close()
