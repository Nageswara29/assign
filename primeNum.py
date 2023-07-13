num = int(input("Enter a number\n"))
val=False
if num == 1:
    print(num,"is not a prime number")
else:
    for i in range(2,num):
        if (num%i)==0:
            val=True
            break
    if val:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")