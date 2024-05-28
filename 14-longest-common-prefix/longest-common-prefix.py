class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = []
        min_len = min([len(s) for s in strs])
        for i in range(min_len):
            t=strs[0][i]
            for word in strs:
                if word[i]==t:
                    continue
                else:
                    return "".join(lcp)
            lcp.append(t)
        return "".join(lcp)

            
                
                
