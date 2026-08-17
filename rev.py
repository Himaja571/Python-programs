arr = [1, 2, 3, 4, 5, 6, 7]
d = 3

new_arr = []

for i in range(d, len(arr)):
    new_arr.append(arr[i])

for i in range(d):
    new_arr.append(arr[i])

print(new_arr)