def func(n,i):
    if i<1:
        return
    print(i)
    func(n,i-1)
n=int(input("n:"))
func(n,n)