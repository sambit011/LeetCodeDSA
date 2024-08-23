from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_stones = Counter(stones)
        num_jewels = 0
        for jewel in jewels:
            if jewel in num_stones:
                num_jewels += num_stones[jewel]
                
        return num_jewels