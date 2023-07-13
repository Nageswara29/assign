n=int(input("Enter a number"))
a=n
while(n>0):
    j=n%10
    if j!=0 and j!=1:
        print("Given Number is not binary")
        break
    n=n//10
    if n==0:
        print("Given Number is binary")
