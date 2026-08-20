arr=[1,2,4,5]
n=len(arr)
actual_sum=0
expected_sum=0
for i in range(len(arr)):
    actual_sum+=arr[i]
for i in range(1,n+2):
    expected_sum+=i
print(expected_sum-actual_sum,"is the missing number")

    