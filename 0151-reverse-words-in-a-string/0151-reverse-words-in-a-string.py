class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()

        rev = " "
        for word in words:
            rev = " " + word + rev

        return rev.strip()