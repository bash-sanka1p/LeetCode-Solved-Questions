class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        map={}
        arr=[]
        for n in nums:
            if n not in map.keys():
                map[n]=1
        print(map)
        for i in range(1,len(nums)+1):
            if i not in map.keys():
                arr.append(i)
        
        return arr