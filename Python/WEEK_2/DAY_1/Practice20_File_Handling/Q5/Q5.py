file=open("Q5/data.txt","w+")
file.write("""aditya
abhilash
vivek""")
file.seek(0)
while True:
    line=file.readline()
    if line=="":
        break
    else:
        print(line,end="")
file.close()
