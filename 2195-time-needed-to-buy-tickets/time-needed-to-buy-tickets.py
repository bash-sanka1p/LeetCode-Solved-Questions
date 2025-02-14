class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0
        for i in range(len(tickets)):
            if i < k:
                t+=min(tickets[k], tickets[i])
            if i > k:
                t+=min(tickets[k]-1, tickets[i])
            print(i,t)
        return t+tickets[k]