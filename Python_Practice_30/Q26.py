d1={"Rahul":10,"abhi":99,"Vivek":80}
d2={"Aditya":30,"mahendra":99,"Nishanth":99}
for i in d2:
    d1[i]=d2[i]
print(d1)
print(d1.update(d2))