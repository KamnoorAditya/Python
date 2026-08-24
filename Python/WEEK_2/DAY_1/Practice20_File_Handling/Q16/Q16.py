#Create a file containing a paragraph. Use read() to count the total number of words.
file=open("Q16/data.txt","w+")
file.write("""Hello i am kamfhiuewbfuycg guiugfyawekvyc vyuvaukcyvkv  yvkuaycvkiyvc
ceugyuygc hsbvk uyv u vkuy vuy vui c tciu tc uc uyc t 
 vkucvu tcku c kucy ku""")
file.seek(0)
content=file.read()
count=0
for i in content.split(" "):
    count+=1
print(count) 