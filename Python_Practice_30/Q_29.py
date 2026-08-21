n=int(input())
fact=1
def fact(n:int):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
print(fact(n))
