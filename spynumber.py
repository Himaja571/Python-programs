n=int(input("n:"))
temp=n
sum=0
product=1
while(n>0):
    last_digit=n%10
    sum=sum+last_digit
    product=product*last_digit
    n=n//10
if sum==product:
    print(temp,"is a spy number")
else:
    print(temp,"is not a spy number")