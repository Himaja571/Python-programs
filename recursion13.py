def f(n):
    if n<=1:
        return n
    last=f(n-1)
    slast=f(n-2)
    return (f(n-1)+f(n-2))
n=int(input("n:"))
print(f(n))
