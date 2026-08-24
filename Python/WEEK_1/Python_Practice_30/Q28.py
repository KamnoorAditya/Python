n=int(input())
l1=[]
for i in range(n):
    l1.append(int(input()))

def find_largest(l1):
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    print(max)
find_largest(l1)