class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        if N == 0:
            return []
        a = nums[0]
        b = nums[0]
        ans = []
        for i in range(1,N):
            if nums[i] == b+1:
                b = nums[i]
            else:
                if(a!=b):
                    ans.append(str(a)+'->'+str(b))
                else:
                    ans.append(str(a))
                    
                a=nums[i]
                b=nums[i]
        
        if(a!=b):
            ans.append(str(a)+'->'+str(b))
        else:
            ans.append(str(a))
            
        return ans