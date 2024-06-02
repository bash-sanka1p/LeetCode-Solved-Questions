class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for ele in nums:
            if ele in map.keys():
                map[ele]+=1
            else:
                map[ele]=1
        max_count_key=max(map,key=map.get)
        return max_count_key