def func(i):
   if i>len(arr)//2:
       return
   arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
   func(i+1)
arr=list(map(int,input("Enter array elements:").split()))
n=len(arr)
func(0)
print( "reversed array using recursion:",arr)