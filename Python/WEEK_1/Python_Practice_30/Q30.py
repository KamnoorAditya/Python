n=int(input())
def find_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return(sum)
print(find_sum(n))