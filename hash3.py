
n=int(input("n:"))
arr=[]
for i in range(n):
    num=int(input("num:"))
    arr.append(num)
print(arr)
mpp= {}
for i in range(n):
    if arr[i] in mpp:
        mpp[arr[i]]+=1
    else:
        mpp[arr[i]]=1



q=int(input("q:"))
while(q>0):
    m=int(input("m:"))
    print(mpp.get(m,0))
    q-=1
