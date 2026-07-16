numbers = [10, 20, 30, 40, 50]

print("Original List :", numbers)

# Length
print("Length :", len(numbers))

# Append
numbers.append(60)
print("After append :", numbers)

# Insert
numbers.insert(2, 25)
print("After insert :", numbers)

# Extend
numbers.extend([70, 80])
print("After extend :", numbers)

# Remove
numbers.remove(40)
print("After remove :", numbers)

# Pop
removed = numbers.pop()
print("Popped Element :", removed)
print("After pop :", numbers)

# Index
print("Index of 30 :", numbers.index(30))

# Count
numbers.append(20)
print("Count of 20 :", numbers.count(20))

# Reverse
numbers.reverse()
print("Reverse :", numbers)

# Sort
numbers.sort()
print("Sorted :", numbers)

# Copy
copy_list = numbers.copy()
print("Copied List :", copy_list)

# Maximum
print("Maximum :", max(numbers))

# Minimum
print("Minimum :", min(numbers))

# Sum
print("Sum :", sum(numbers))

# Check Membership
print("20 in list :", 20 in numbers)
print("100 in list :", 100 in numbers)

# Iterating through List
print("\nElements:")
for i in numbers:
    print(i)

# Access using Index
print("\nFirst Element :", numbers[0])
print("Last Element :", numbers[-1])

# Slicing
print("First 3 Elements :", numbers[:3])
print("Last 3 Elements :", numbers[-3:])
print("Middle Elements :", numbers[2:5])

# Update Element
numbers[1] = 100
print("After Updating Index 1 :", numbers)

# Delete using del
del numbers[2]
print("After del :", numbers)

# Concatenation
list2 = [200, 300]
new_list = numbers + list2
print("Concatenated List :", new_list)

# Repetition
print("Repeated List :", list2 * 3)

# Clear
temp = new_list.copy()
temp.clear()
print("After clear :", temp)

# Nested List
nested = [[1, 2], [3, 4], [5, 6]]
print("Nested List :", nested)
print("First Element of Second List :", nested[1][0])

# List Comprehension
square = [x*x for x in numbers]
print("Squares :", square)

# Even Numbers
even = [x for x in numbers if x % 2 == 0]
print("Even Numbers :", even)

# Odd Numbers
odd = [x for x in numbers if x % 2 != 0]
print("Odd Numbers :", odd)

# Largest and Smallest
print("Largest :", max(numbers))
print("Smallest :", min(numbers))

# Sorting Descending
desc = sorted(numbers, reverse=True)
print("Descending :", desc)