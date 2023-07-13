def palindrome(n,temp):
    if n==0:
        return temp
    temp=temp*10+n%10
    return palindrome(n//10,temp)


n=int(input("Enter a number\n"))
temp=palindrome(n,0)

if temp==n:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")

