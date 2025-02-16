class Solution:
    def mergeSort(self, nums, left, right):
        if left == right: return nums

        mid = (left + right) // 2 
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)
        self.merge(nums, left, mid, right)
        return nums
    
    def merge(self, nums, left, mid, right):
        l_arr, r_arr = nums[left:mid+1], nums[mid+1: right+1]
        i, j, k = left, 0, 0

        while j<len(l_arr) and k<len(r_arr):
            if l_arr[j]<= r_arr[k]:
                nums[i] = l_arr[j]
                j+=1
            else:
                nums[i] = r_arr[k]
                k+=1
            i+=1

        while j<len(l_arr):
            nums[i] = l_arr[j]
            j+=1
            i+=1
        
        while k<len(r_arr):
            nums[i] = r_arr[k]
            k+=1
            i+=1

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums, 0, len(nums))
        





