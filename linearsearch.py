# Linear Search Program

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Create an empty list
arr = []

# Input elements
print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Input the element to search
target = int(input("Enter the element to search: "))

# Perform Linear Search
found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Element found at index {i}")
        found = True
        break

if not found:
    print("Element not found")