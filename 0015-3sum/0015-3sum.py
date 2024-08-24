class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)
                    
        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i + 1, n - 1

            while lo < hi:
                summ = nums[i] + nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo, hi = lo + 1, hi - 1
                    while lo < hi and nums[lo - 1] == nums[lo]:
                        lo += 1
                    while lo < hi and nums[hi + 1] == nums[hi]:
                        hi -= 1
                elif summ < 0:
                    lo += 1
                else:
                    hi -= 1
            
        return answer