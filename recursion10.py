def func(l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    func(l+1,r-1)
arr= list(map(int, input("Enter array elements: ").split()))

func(0,len(arr)-1)
print("reversed array:",arr)
    