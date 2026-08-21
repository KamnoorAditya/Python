l1=[10, 20, 10, 30, 20, 40, 30]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)