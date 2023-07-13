num1=int(input("Enter first number\n"))
num2=int(input("Enter second number\n"))
num3=int(input("Enter Three number\n"))

if num1>=num2 and num1>=num3:
    l=num1
elif num2>=num1 and num2>=num3:
    l=num2
else:
    l=num3
print("The largest number is",l)