def func(n):
    if n==0:
        return 0
    return(n+func(n-1))
n=int(input("n:"))
print(func(n))