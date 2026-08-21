marks = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 78,
    "Sneha": 95
}
highest = 0
student = ""
for name in marks:
    if marks[name] > highest:
        highest = marks[name]
        student = name

print(student)
print(highest)