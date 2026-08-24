#Read a file containing numbers and use a for loop to print only the even numbers.
file=open("Q8/data.txt","w+")
file.write("""10
20
30
40
50
45
67
60""")
file.seek(0)
for i in file:
    if int(i)%2==0:
        print(i)
file.close()