def  f(i,str):
    if i>=len(str)//2:
        return True
    if str[i]!=str[len(str)-i-1]:
      return False
    return f(i+1,str)
str=input("Enter string:")
print(f(1,str))
