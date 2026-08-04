n=int(input("n:"))
temp=n
sum=0
while(n>0):
    last_digit=n%10
    fact=1
    for i in range(1,last_digit+1):
        fact=fact*i
    sum=sum+fact
    n=n//10
if temp==sum:
    print(temp,"is a strong number")
else:
    print(temp,"is not a strong number")