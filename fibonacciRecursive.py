def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


n=int(input("How many terms?\n"))
if n <= 0:
    print("Please enter a positive integer")
else:
    for i in range(n):
        print(fibonacci(i))