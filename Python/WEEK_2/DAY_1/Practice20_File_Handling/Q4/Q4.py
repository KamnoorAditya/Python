file=open("Q4/Numbers.txt","r")
content=file.readlines()
sum=0
for i in content:
    sum+=int(i)
print(sum)
