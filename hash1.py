n=int(input("n:"))
arr=[]
for i in range(n):
   num=int(input("num:"))
   arr.append(num)

hash=[0]*101
for i in range(n):
     hash[arr[i]]+=1


q=int(input("q:"))
while(q>0):
    m=int(input("m:"))
    print(hash[m])
    q-=1