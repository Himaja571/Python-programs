n = int(input("Enter number of elements: "))

lst = []

for i in range(n):
    lst.append(int(input()))

result = []

for item in lst:
    if item not in result:
        result.append(item)

print("Original List:", lst)
print("Without Duplicates:", result)