def func(i,sum):
    if i<1:
        print(sum)
        return
    func(i-1,sum+i)
n=int(input("n:"))
func(n,0)