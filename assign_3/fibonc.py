def fib(x):
    if x<=0:
        return 0
    elif x==1:
        return 0
    else:
        return fib(x-1)+fib(x-2)+1
result=fib(7)
print(result)
