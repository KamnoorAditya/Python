#Create a file students.txt and write 5 student names into it using write().
file=open("Q11/students.txt","w")
content="""Hello
Aditya
Abhishek
Vivek
Nishanth
Mahendra"""
file.write(content)
file.seek(0)
file.close()