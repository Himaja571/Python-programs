text="banana"
frq={}
for char in text:
   frq[char]   = frq.get(char, 0) + 1
print(frq)
   