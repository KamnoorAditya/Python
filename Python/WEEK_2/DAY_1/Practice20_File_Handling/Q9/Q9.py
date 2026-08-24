#Read a file containing names and print only names whose length is greater than 5.
file=open("Q9/data.txt","w+")
content="""Aditya
abhishek
nishanth
vivek
mahi"""
file.write(content)
file.seek(0)
list1=file.read()
for i in list1.split():
    if len(i)>5:
        print(i)
file.close()