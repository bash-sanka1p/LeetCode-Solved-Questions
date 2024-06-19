class Solution:
    def maxScore(self, s: str) -> int:
        scores=[]
        for i in range(1,len(s)):
            score=s[:i].count('0')+s[i:].count('1')
            print(score)
            scores.append(score)

        return max(scores)