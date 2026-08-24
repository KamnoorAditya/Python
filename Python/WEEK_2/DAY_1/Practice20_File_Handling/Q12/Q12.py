#Create a file and write numbers from 1 to 10, with each number on a separate line.
file=open("Q12/numbers.txt","w+")
for i in range(1,11):
    file.write(str(i) +"\n")
file.close()
