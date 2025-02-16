class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,101):
            cnt=0
            for x in nums:
                if x>=i:
                    cnt+=1
            if cnt==i: return i
        return -1
        