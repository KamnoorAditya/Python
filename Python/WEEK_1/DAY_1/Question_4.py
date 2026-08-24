age=int(input("Enter your age: "))
has_id=input("Do you have your ID?").lower() == "yes"
if(age>=18 and has_id):
    print("Allowed")
else:
    print("Not Allowed")