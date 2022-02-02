#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        print(low, high, arr)
        if low == high:
            return
        pivot = arr[high]
        i = low-1
        for j in range(low, high+1):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        if i >= 1:
            self.quickSort(arr, 0, i-1)
        if i<high:
            self.quickSort(arr, i+1, high)
        
        
    
A = [5,4,3,2,1]
Solution().quickSort(A, 0, len(A)-1)
print(A)
