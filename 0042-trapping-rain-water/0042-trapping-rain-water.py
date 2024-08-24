class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        total_water = 0
        l_wall = 0
        r_wall = 0
        max_l = [0] * n
        max_r = [0] * n
        
        for i in range(n):
            j = -i - 1
            max_l[i] = l_wall
            max_r[j] = r_wall
            l_wall = max(l_wall ,height[i])
            r_wall = max(r_wall, height[j])
            
            
        for i in range(n):
            pot = min(max_l[i], max_r[i]) - height[i]
            if pot > 0:
                total_water += pot
        
        return total_water