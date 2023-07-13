n=int(input("Enter a number\n"))
a=0
b=n
while b>0:
    a=a*10+b%10
    b=b//10
if a==n:
    print(n,"is a polindrome")
else:
    print(n,"is not a polindrome")