from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = Counter(magazine)
        ransom_letters = Counter(ransomNote)
        
        for letter, freq in ransom_letters.items():
            if freq > mag_letters[letter]:
                return False
        return True