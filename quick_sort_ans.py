#User function Template for python3

class Solution:
    # A typical recursive Python
    # implementation of QuickSort
    
    # Function takes last element as pivot,
    # places the pivot element at its correct
    # position in sorted array, and places all
    # smaller (smaller than pivot) to left of
    # pivot and all greater elements to right
    # of pivot
    def partition(self, arr, low, high):
        i = (low - 1)         # index of smaller element
        pivot = arr[high]     # pivot
    
        for j in range(low, high):
    
            # If current element is smaller 
            # than or equal to pivot
            if arr[j] <= pivot:
            
                # increment index of
                # smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
    
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)
    
    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low --> Starting index,
    # high --> Ending index
    
    # Function to do Quick sort
    def quickSort(self, arr, low, high):
        print(low, high, arr)
        if low < high:
    
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)
    
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi + 1, high)


A = [7,5,4,3,2,1]

Solution().quickSort(A, 0, len(A)-1)
print(A)