class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for s in strs:
            sorteds="".join(sorted(s))
            if sorteds not in map:
                map[sorteds]=[s]
            else:
                map[sorteds].append(s)
        return map.values()

