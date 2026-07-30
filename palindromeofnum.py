n=int(input("n:"))
original=n
reversed_num=0
while(n>0):
    rev=n%10
    reversed_num=reversed_num*10+rev
    n=n//10
if original==reversed_num:
        print(original,"is a palindrome")
else:
        print(original,"is not a palindrome")