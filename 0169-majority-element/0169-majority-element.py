from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key, values in freq.items():
            if values > len(nums)//2:
                return key