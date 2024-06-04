class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index=-1
        for i in range(len(nums)):
            lsum=sum(nums[:i])
            rsum=sum(nums[i+1:])
            if i==0:lsum=0 
            elif i==len(nums)-1: rsum=0
            print(lsum,rsum)
            if lsum==rsum:
                index=i
                break
        return index