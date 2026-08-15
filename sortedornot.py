arr=[]
n=int(input("enter the range of numbers:"))
print("enter the numbers")
for i in range(n):
    arr.append(int(input()))
for i in range(1,len(arr)):
    if arr[i]<arr[i-1]:
      print(False)
      break   
else:
      print(True)  

