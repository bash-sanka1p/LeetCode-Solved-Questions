class Solution:
    def mergeSort(self, arr, left, right):
        if left==right:
            return arr
        mid = (left+right) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid+1, right)
        self.merge(arr, left, mid, right)

        return arr
    def merge(self, arr, left, mid, right):
        l_arr, r_arr = arr[left:mid+1], arr[mid+1: right+1]
        i, j, k = left, 0, 0

        while j<len(l_arr) and k<len(r_arr):
            if l_arr[j] <= r_arr[k]:
                arr[i] = l_arr[j]
                j+=1
            else:
                arr[i] = r_arr[k]
                k+=1
            i+=1
        
        while j < len(l_arr):
            arr[i] = l_arr[j]
            i+=1
            j+=1

        while k < len(r_arr):
            arr[i] = r_arr[k]
            i+=1
            k+=1
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums))
        return nums     



