#Ask the user to enter two numbers and calculate their sum. Handle the situation where the user enters text instead of a number using try-except.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Sum =", num1 + num2)

except ValueError:
    print("Please enter valid numbers.")