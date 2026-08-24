#Read a file line by line using a for loop and print every line.
file=open("Q7/data.txt","r")
for i in file:
    print(i,end=" ")
file.close()