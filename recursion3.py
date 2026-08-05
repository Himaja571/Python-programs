def f(i,n):
    if i>n:
        return
    print(i)
    
    f(i+1,n)
n=int(input("n:"))
f(1,n)

    