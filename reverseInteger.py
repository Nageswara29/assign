num=int(input("Enter a number\n"))
rev_num=0
while num != 0:
    n=num%10
    rev_num=rev_num*10+n
    num //= 10
print("Reversed Number: " + str(rev_num))