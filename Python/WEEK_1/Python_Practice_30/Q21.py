l1=[10,20,30,20,30,40,50,10]
s1=set()
for i in l1:
    if i not in s1:
        s1.add(i)
print(s1)