def fibonacci(n):
    x=0
    y=1
    i=0
    print(x)
    print(y)
    while i<=n:
        sum=x+y
        print(sum)
        x=y
        y=sum
        i+=1

fibonacci(10)
