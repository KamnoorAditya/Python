n=int(input())
digit=0
copy=n
count=0
while(n>0):
    digit=n%10
    if(digit%2==0):
        count+=1
    n//=10
print(f"Total even digits in {copy} are {count}")