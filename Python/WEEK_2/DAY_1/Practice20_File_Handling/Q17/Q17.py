file = open("Q17/data.txt", "w+")

file.write("""10
20
30
40
50
60
70
80
90
100""")

file.seek(0)

total = 0

content = file.readlines()

for i in content:
    total += int(i)

avg = total / len(content)

print(avg)

file.close()