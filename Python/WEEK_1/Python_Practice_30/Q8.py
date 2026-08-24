s1=input()
longest=""
words=s1.split(" ")
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)
