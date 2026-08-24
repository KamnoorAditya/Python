l1=[10,20,30,40,50]
first=l1[0]
second=l1[0]
for i in l1:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)