# Binary Search Program

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Create an empty list
arr = []

# Input elements
print("Enter the elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Sort the list
arr.sort()

print("Sorted List:", arr)

# Input the element to search
target = int(input("Enter the element to search: "))

# Binary Search
low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print(f"Element found at index {mid}")
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")