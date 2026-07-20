rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter First Matrix")
A = []
for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter Second Matrix")
B = []
for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(rows):
    temp = []
    for j in range(cols):
        temp.append(A[i][j] + B[i][j])
    C.append(temp)

print("Result Matrix")

for row in C:
    print(row)