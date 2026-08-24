#Read a file containing numbers and find the largest and smallest number using a for loop.
file=open("Q10/data.txt","w+")
content="""30
40
567
762
98989"""
file.write(content)
file.seek(0)
l=file.readlines()
max=int(l[0])
min=int(l[0])
for i in l:
    if int(i)>max:
        max=int(i)
    if int(i)<min:
        min=int(i)
print(max)
print(min)
file.close()