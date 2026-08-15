n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements: ")))
smallest=arr[0]
second_smallest= arr[1]
for i in range(2,len(arr)):
   if arr[i]<smallest:
       second_smallest=smallest
       smallest=arr[i]
   elif arr[i]<second_smallest and arr[i]!=smallest:
            second_smallest=arr[i]
print(f"{second_smallest} is the second smallest element in the array.")