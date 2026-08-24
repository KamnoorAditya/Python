file=open("practice.py","w")
file.write("from datetime import datetime \n"
"date_today=datetime.now() \n"
"print(date_today)\n")
content=file.read()
print(content)

file.close()

file=open("practice.py","a")
file.write("""print("added a new line")""")
file.close()
