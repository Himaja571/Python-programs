def display(i,n):
    if i>n:
        return
    print("Python programming")
    display(i+1,n)
n=int(input("n:"))
display(1,n)