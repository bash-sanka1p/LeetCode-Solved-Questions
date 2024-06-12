class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums)==1:return True
        sign=-1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                sign=1
                break
            elif nums[i]>nums[i+1]:
                sign=-1
                break
            else: pass
        for i in range(len(nums)-1):
            if sign==-1 and nums[i]>=nums[i+1]:
                continue
            elif sign==1 and nums[i]<=nums[i+1]:
                continue
            else: return False
        return True