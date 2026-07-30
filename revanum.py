n=int(input("n:"))
reversed_num=0
while(n>0):
    
       reversed = n % 10
        reversed_num=(reversed_num*10)+reversed
        n=n//10
    
    
print(reversed_num)