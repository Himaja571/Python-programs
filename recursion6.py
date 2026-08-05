def func(n,i):
    if i>n:
        return
    func(n,i+1)
    print(i)
n=int(input("n:"))
func(n,1)