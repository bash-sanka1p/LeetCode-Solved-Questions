class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        pairs=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and i<j:
                    pairs+=1
    
        return pairs