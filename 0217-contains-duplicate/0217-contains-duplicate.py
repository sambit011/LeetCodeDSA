from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_nums = Counter(nums)
        for _ , val in freq_nums.items() :
            if val > 1:
                return True
        return False