import math
num=float(input("enter a number to find its logarithm: "))
if num>0:
    print("logarithm of",num,"is",math.log(num))
else:
    result=math.log(num)
    print("The logarithm of", num, "is", result)
