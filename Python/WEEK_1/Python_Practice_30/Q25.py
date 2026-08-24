sentence=input().split(" ")
count=0
d1={}
for i in sentence:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
print(d1)