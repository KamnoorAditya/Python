l1=[10,20,30,4]
smallest=l1[0]
largest=l1[0]
for i in l1:
    if i<smallest:
        smallest=i
    if i>largest:
        largest=i
print(f"smallest is {smallest} , largest is {largest} ")
