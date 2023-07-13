n=int(input("How many terms?\n"))
n1,n2=0,1
count=0
if n<=0:
    print("Please enter a positive integer")
elif n==1:
    print(n1)
else:
    while count < n:
        print(n1)
        x=n1+n2
        n1=n2
        n2=x
        count += 1
