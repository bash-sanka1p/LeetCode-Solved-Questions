class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from  collections import Counter
        freq = Counter(nums)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(sorted_freq)
        res = [x for x, _ in sorted_freq[:k]]
        return res
        