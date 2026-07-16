t = (10, 20, 30, 40, 50)

print("Original Tuple :", t)

# Length
print("Length :", len(t))

# Access Elements
print("First Element :", t[0])
print("Last Element :", t[-1])

# Slicing
print("First 3 Elements :", t[:3])
print("Last 3 Elements :", t[-3:])
print("Middle Elements :", t[1:4])

# Count
print("Count of 20 :", t.count(20))

# Index
print("Index of 30 :", t.index(30))

# Maximum
print("Maximum :", max(t))

# Minimum
print("Minimum :", min(t))

# Sum
print("Sum :", sum(t))

# Membership
print("30 in Tuple :", 30 in t)
print("100 in Tuple :", 100 in t)

# Iteration
print("\nElements:")
for i in t:
    print(i)

# Concatenation
t2 = (60, 70)
new_tuple = t + t2
print("\nConcatenated Tuple :", new_tuple)

# Repetition
print("Repeated Tuple :", t2 * 3)

# Sorting
print("Sorted Tuple :", tuple(sorted(t, reverse=False)))

# Reverse Sorting
print("Descending Order :", tuple(sorted(t, reverse=True)))

# Convert Tuple to List
lst = list(t)
print("Tuple to List :", lst)

# Modify the List
lst.append(60)
print("After Appending to List :", lst)

# Convert List back to Tuple
t3 = tuple(lst)
print("List to Tuple :", t3)

# Nested Tuple
nested = ((1, 2), (3, 4), (5, 6))
print("\nNested Tuple :", nested)
print("First Element of Second Tuple :", nested[1][0])

# Unpacking
a, b, c, d, e = t
print("\nTuple Unpacking:")
print(a, b, c, d, e)

# Enumerate
print("\nEnumerate:")
for index, value in enumerate(t):
    print(index, value)

# Largest and Smallest
print("\nLargest :", max(t))
print("Smallest :", min(t))

# Tuple from String
s = "Python"
t4 = tuple(s)
print("\nTuple from String :", t4)

# Tuple from List
l = [100, 200, 300]
t5 = tuple(l)
print("Tuple from List :", t5)