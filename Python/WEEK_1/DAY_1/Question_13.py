num=[12,5,8,21,4,15,10]
sum=0
for i in num:
    sum+=i
small=num[0]
largest=num[0]
for i in num:
    if i<small:
        small=i
for i in num:
    if(i>largest):
        largest=i
print(largest)
print(small)
print(sum)