n=int(input("enter the range:"))
arr=[]
for i in range(n):
    num=int(input("num:"))
    arr.append(num)
print("insertion sort")
print("orginal array:",arr)
for i in range(n):
    for j in range(n):
        while(j>0 and arr[j-1]>arr[j]):
         arr[j-1],arr[j]=arr[j],arr[j-1]
         j-=1
         
print("sorted array:",arr)