def func(n,i):
    if i<1:
        return
    func(n,i-1)
    print(i)
n=int(input("n:"))
func(n,n)