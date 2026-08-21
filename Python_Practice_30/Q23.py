d1={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
name=""
max=0
for i,j in d1.items():
    if j>max:
        max=j
        name=i
print(max)
print(name)