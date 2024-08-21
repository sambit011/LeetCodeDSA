class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        merged = ''
        for i in range(n):
            merged+=word1[i]+word2[i]
            
        diff = len(word1)-len(word2)
        
        if diff < 0:
            merged+=word2[diff:]
        elif diff > 0:
            merged+= word1[-diff:]
        
        return merged
            