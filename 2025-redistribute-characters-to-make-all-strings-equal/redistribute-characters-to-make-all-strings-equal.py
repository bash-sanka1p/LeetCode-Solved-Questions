class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hmap = {}
        for word in words:
            for c in word:
                if not c in hmap.keys():
                    hmap[c]=1
                else:
                    hmap[c]+=1
        for occurance in hmap.values():
            if occurance%len(words) != 0:
                return False
        return True