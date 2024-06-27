import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -(sys.maxsize - 1)
        arr_sum = 0
        for i in nums:
            arr_sum += i
            max_sum = max(max_sum, arr_sum)
            if arr_sum < 0:
                arr_sum = 0

        return max_sum
