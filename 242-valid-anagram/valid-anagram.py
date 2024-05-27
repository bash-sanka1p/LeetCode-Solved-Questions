class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1={}
        hmap2={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in hmap1:
                hmap1[s[i]]+=1
            else:
                hmap1[s[i]]=1

            if t[i] in hmap2:
                hmap2[t[i]]+=1
            else:
                hmap2[t[i]]=1
        print(hmap1, hmap2)
        return hmap1==hmap2
            