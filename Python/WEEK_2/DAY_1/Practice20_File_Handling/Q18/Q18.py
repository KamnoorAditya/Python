#Create a file containing several names. Read the file using a for loop and count how many names are present.
file=open("Q18/data.txt","w+")
content="""
hello
i
iam
gt
hth
thdh
eh
evb6u
b56
u"""
file.write(content)
file.seek(0)
content=file.readlines()
print(len(content))
file.close() 