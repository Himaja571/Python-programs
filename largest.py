arr=[]
n=int(input("Enter the range of numbers:"))
for i in range(n):
    num=int(input("num:"))
    arr.append(num)
largest=arr[0]
for i in range(n):
    if arr[i]>largest:
        largest=arr[i]
print("largest element in given array",largest)
