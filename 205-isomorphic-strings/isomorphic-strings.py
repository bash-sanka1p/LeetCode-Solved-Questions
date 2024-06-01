class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        tmp=set(list(zip(s,t)))
        if len(set(s))!=len(set(t)): return False
        if len(set(s))!=len(tmp): return False
        return True