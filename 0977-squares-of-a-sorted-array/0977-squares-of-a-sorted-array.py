class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        answer = []
        while(l <= r):
            if(abs(nums[l]) < abs(nums[r])):
                answer.insert(0 , nums[r]**2)
                r -= 1
            else:
                answer.insert(0, nums[l]**2)
                l += 1
        return answer