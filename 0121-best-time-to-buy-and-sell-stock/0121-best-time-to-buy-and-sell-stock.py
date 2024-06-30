import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minPrice = float('inf')

        for price in prices:
            minPrice = min(minPrice, price)
            maxProf = max(maxProf, price-minPrice)
        
        return maxProf