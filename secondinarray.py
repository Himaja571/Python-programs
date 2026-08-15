'''n=int(input("Enter the number of elements in the array: "))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements: ")))
maximum=arr[0]
second_maximum=arr[0]
for i in range(1,n):
    if arr[i]>maximum:
        second_maximum=maximum
        maximum=arr[i]
    elif arr[i]>second_maximum and arr[i]!=maximum:
        second_maximum=arr[i] 
smallest=arr[0]
second_smallest= arr[1]
for i in range(1,len(arr)):
   if arr[i]<smallest:
       second_smallest=smallest
       smallest=arr[i]
   elif arr[i]<second_smallest and arr[i]!=smallest:
            second_smallest=arr[i]
print(second_smallest,second_maximum)'''
