student = {
    "id": 571,
    "name": "Himaja",
    "age": 20,
    "course": "CSE",
    "cgpa": 8.58
}

print("Original Dictionary :", student)

# Length
print("Length :", len(student))

# Access Value
print("Name :", student["name"])

# Using get()
print("Course :", student.get("course"))

# Get Non-existing Key
print("Phone :", student.get("phone", "Not Available"))

# Keys
print("Keys :", student.keys())

# Values
print("Values :", student.values())

# Items
print("Items :", student.items())

# Add New Key
student["city"] = "Hyderabad"
print("After Adding City :", student)

# Update Value
student["age"] = 21
print("After Updating Age :", student)

# Update Multiple Values
student.update({"cgpa": 8.75, "branch": "CSE-AI"})
print("After Update :", student)

# Membership
print("'name' in Dictionary :", "name" in student)
print("'salary' in Dictionary :", "salary" in student)

# Pop
removed = student.pop("branch")
print("Removed :", removed)
print("After Pop :", student)

# Popitem
item = student.popitem()
print("Popitem :", item)
print("After Popitem :", student)

# Set Default
student.setdefault("country", "India")
print("After setdefault :", student)

# Copy
copy_dict = student.copy()
print("Copied Dictionary :", copy_dict)

# Iterating Keys
print("\nKeys:")
for key in student:
    print(key)

# Iterating Values
print("\nValues:")
for value in student.values():
    print(value)

# Iterating Keys and Values
print("\nKey : Value")
for key, value in student.items():
    print(key, ":", value)

# Maximum and Minimum Key
print("\nMaximum Key :", max(student))
print("Minimum Key :", min(student))

# Dictionary from Keys
keys = ["A", "B", "C"]
new_dict = dict.fromkeys(keys, 0)
print("Dictionary from Keys :", new_dict)

# Nested Dictionary
employees = {
    101: {"Name": "ramu", "Salary": 50000},
    102: {"Name": "somu", "Salary": 60000}
}

print("\nNested Dictionary :", employees)
print("Employee 101 Name :", employees[101]["Name"])

# Dictionary Comprehension
square = {x: x*x for x in range(1,6)}
print("\nDictionary Comprehension :", square)

# Clear
temp = student.copy()
temp.clear()
print("After Clear :", temp)