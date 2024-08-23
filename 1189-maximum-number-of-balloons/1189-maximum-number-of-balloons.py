from collections import Counter
import sys
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        min_letters = sys.maxsize
        for letter in "balon":
            if letter =='l' or letter == 'o':
                min_letters = min(min_letters, freq[letter]//2)
            else:
                min_letters = min(min_letters, freq[letter])
        
        return min_letters