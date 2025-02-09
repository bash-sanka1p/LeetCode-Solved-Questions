class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [-1, -1]
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n]+=1
            else:
                hmap[n]=1

        for i in range(1, len(nums)+1):
            if hmap.get(i, 0) == 0:
                res[1] = i
            if hmap.get(i, 0) == 2:
                res[0] = i
        return res


