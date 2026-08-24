t1=(10,20,30,40,50)
max=t1[0]
min=t1[0]
sum=0
for i in t1:
    sum+=i
    if i>max:
        max=i
    if i<min:
        min=i
print(f"Sum is {sum},Max is {max}, Min is {min}")