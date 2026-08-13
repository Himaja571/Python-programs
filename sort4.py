class Solution():
    def merge(self,arr,low,mid,high):
        temp=[]
        left,right=low,mid+1
        while(left<=mid and right<=high):
            if arr[left]<arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        while(right<=high):
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]        
    def mergesort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

arr = []
n = int(input("Enter the number of elements: "))
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))
sol = Solution()
sol.mergesort(arr, 0, len(arr) - 1)
print(*arr)   