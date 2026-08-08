string=input("string:")
q=int(input("enter the number of queries:"))

hash=[0]*101
for i in range(len(string)):
    hash[ord(string[i])-ord('a')]+=1
while(q>0):
    m=input(" m:")
    print(hash[ord(m)-ord('a')])
    q-=1