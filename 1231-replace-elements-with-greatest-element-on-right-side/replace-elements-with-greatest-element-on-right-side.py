class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # maxele=max(arr)
        # for i in range(len(arr)):
        #     if i==len(arr)-1:
        #         arr[i]=-1
        #         return arr
        #     if maxele==arr[i]:
        #         maxele=max(arr[i+1:])
        #     arr[i] = maxele
        maxele=-1
        for i in range(len(arr)-1, -1, -1):
            tempmax=max(arr[i],maxele)
            arr[i]=maxele
            maxele=tempmax
        return arr
