class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map={}
        for ch in text:
            if ch in "balloon":
                if ch not in map.keys():
                    map[ch]=0.0
                if ch=='l' or ch=='o':
                    map[ch]+=0.5
                else:
                    map[ch]+=1
        if sorted(map.keys()) == sorted(set("balloon")):
            return int(min(map.values()))
        return 0
                    
        
        #     return min(vals)
        # else: return 0