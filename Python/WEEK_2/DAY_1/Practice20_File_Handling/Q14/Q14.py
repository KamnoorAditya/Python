#Take 5 numbers from the user and write them into a file, one number per line.
file=open("Q14/data.txt","w+")
for i in range(5):
    file.write(input()+"\n")