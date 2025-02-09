class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        longest=-1
        for i in range(len(s)):
            current_char=s[i]
            # print("current_char",current_char)
            start = i
            for j in range(len(s[start+1:])):
                c = s[start+1+j]
                if c == current_char:
                    end = start + 1 + j
                    # print(start,end, end-start-1)
                    if longest < len(s[start:end])-1:
                        longest = len(s[start:end])-1
        return longest