from collections import defaultdict

class Solution:
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict = defaultdict(list)
        
        for s in strs:
            key = [0] * 26
            for ch in s:
                key[ord(ch) - ord('a')] += 1
            
            key = tuple(key)
            anagram_dict[key].append(s)
            
        return anagram_dict.values()
        