s = {10, 20, 30, 40, 50}

print("Original Set :", s)

# Length
print("Length :", len(s))

# Add
s.add(60)
print("After add :", s)

# Update
s.update([70, 80, 90])
print("After update :", s)

# Remove
s.remove(20)
print("After remove :", s)

# Discard
s.discard(100)      # No error if element not found
print("After discard :", s)

# Pop
removed = s.pop()
print("Popped Element :", removed)
print("After pop :", s)

# Copy
copy_set = s.copy()
print("Copied Set :", copy_set)

# Maximum
print("Maximum :", max(s))

# Minimum
print("Minimum :", min(s))

# Sum
print("Sum :", sum(s))

# Membership
print("30 in set :", 30 in s)
print("200 in set :", 200 in s)

# Iteration
print("\nElements:")
for i in s:
    print(i)

# Another Set
s2 = {40, 50, 60, 70, 100}

print("\nSecond Set :", s2)

# Union
print("Union :", s.union(s2))

# Intersection
print("Intersection :", s.intersection(s2))

# Difference
print("Difference (s - s2) :", s.difference(s2))

# Symmetric Difference
print("Symmetric Difference :", s.symmetric_difference(s2))

# issubset
print("{40,50} subset of s2 :", {40,50}.issubset(s2))

# issuperset
print("s2 is superset of {40,50} :", s2.issuperset({40,50}))

# isdisjoint
print("{1,2} disjoint with s :", {1,2}.isdisjoint(s))

# Clear
temp = s.copy()
temp.clear()
print("After clear :", temp)

# Frozen Set
fs = frozenset([1,2,3,4])
print("Frozen Set :", fs)

# Convert List to Set
lst = [10,20,20,30,40,40,50]
print("List :", lst)
print("Unique Elements :", set(lst))

# Sorting
print("Sorted Set :", sorted(s))

# Maximum and Minimum
print("Largest :", max(s))
print("Smallest :", min(s))