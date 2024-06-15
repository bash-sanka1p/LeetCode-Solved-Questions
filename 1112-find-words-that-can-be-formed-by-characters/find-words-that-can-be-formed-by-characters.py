class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count=0
        original_chars=chars
        chars=list(original_chars)
        flag=True
        for word in words:
            for ch in word:
                if ch in chars:
                    chars.remove(ch)
                else:
                    flag=False
                    break
            if flag: count+=len(word)
            else: flag=True
            chars=list(original_chars)

       
        return count



