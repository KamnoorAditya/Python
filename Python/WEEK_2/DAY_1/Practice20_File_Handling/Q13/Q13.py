#Take 5 names from the user using input() and write them into a file.
file=open("Q13/data.txt","w+")
for i in range(5):
    file.write(input()+"\n")
file.close()